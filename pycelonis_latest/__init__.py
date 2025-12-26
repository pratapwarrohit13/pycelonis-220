"""Module to interact with EMS services.

This module serves as entry point to all high-level functionality within the EMS.
"""

import logging
import os
import re
import typing

import httpx
from httpx._types import ProxyTypes
from packaging.version import parse
from pycelonis.__version__ import __version__
from pycelonis.celonis import Celonis
from pycelonis.service.team.service import TeamService
from pycelonis_core.client.client import APITokenType, Client, KeyType
from pycelonis_core.utils.errors import PyCelonisError, PyCelonisPermissionError, PyCelonisValueError
from pycelonis_core.utils.ml_workbench import (
    CELONIS_API_TOKEN_ENV,
    CELONIS_KEY_TYPE_ENV,
    CELONIS_URL_ENV,
    TRACKING_LOGGER,
    is_running_in_ml_workbench,
    setup_ml_workbench_logging,
    setup_ml_workbench_tracking,
)

logger = logging.getLogger("pycelonis")


if is_running_in_ml_workbench():
    # If app is running in ML Workbench, specific logging configuration is applied here.
    # Otherwise the surrounding application should take care of configuring the logging.
    setup_ml_workbench_logging()
    setup_ml_workbench_tracking()


def get_celonis(
    base_url: typing.Optional[str] = None,
    api_token: typing.Optional[APITokenType] = None,
    key_type: typing.Optional[typing.Union[str, KeyType]] = None,
    user_agent: typing.Optional[str] = None,
    proxies: typing.Optional[ProxyTypes] = None,
    connect: bool = True,
    permissions: bool = True,
    check_if_outdated: bool = True,
    retries: int = 0,
    delay: int = 1,
    **kwargs: typing.Any,
) -> Celonis:
    """Get a Celonis object.

    Args:
        base_url: Celonis base URL.
        api_token: Celonis API token.
        key_type: KeyType of API token. One of [`APP_KEY`, `USER_KEY`] or [pycelonis_core.client.KeyType][].
        user_agent: Session header value for `User-Agent`.
        proxies: Web proxy server URLs passed on to the httpx client
            [HTTPX Proxying](https://www.python-httpx.org/advanced/#http-proxying)
        connect: If True connects to Celonis on initialization
            (initial request to check if the `token` & `key_type` combination is correct).
        permissions: If True provides permission information.
        check_if_outdated: If true checks if current pycelonis version is outdated.
        retries: Number of total retries if request is failing.
        delay: Delay between retries in seconds.

    Returns:
        The Celonis object.

    Examples:
        Connecting to EMS using CELONIS_API_TOKEN and CELONIS_URL environmental variables:
        ```python
        celonis = get_celonis()
        ```

        Connecting with a different set of credentials:
        ```python
        celonis = get_celonis(
            base_url="<url>", api_token="<api_token>", key_type="<key_type>"
        )
        ```

        Connecting with a dynamic set of credentials:
        ```python
        def get_api_token():
            # Obtain credentials dynamically (e.g. during an OAuth 2.0 flow).
            pass

        celonis = get_celonis(
            base_url="<url>", api_token=get_api_token, key_type="<key_type>"
        )
        ```

        Initialising object without testing connection and reading permissions:
        ```python
        celonis = get_celonis(connect=False, permissions=False)
        ```

        Connecting with httpx web proxies:
        ```python
        from urllib.request import getproxies()
        celonis = get_celonis(proxies=getproxies())
        ```
    """
    base_url = base_url or _read_url_from_env()
    api_token = api_token or _read_api_token_from_env()
    key_type = key_type or _read_key_type_from_env()
    user_agent = user_agent or "pycelonis/" + __version__

    if check_if_outdated:
        _check_if_outdated()

    base_url = _check_url(base_url)
    client = _infer_client(base_url, api_token, key_type, user_agent, proxies, retries=retries, delay=delay, **kwargs)

    if connect:
        _connect(client)

    celonis = Celonis(client)

    if permissions:
        _print_permissions(celonis)

    logging.getLogger(TRACKING_LOGGER).disabled = _is_tracking_disabled(celonis)
    return celonis


def _read_url_from_env() -> str:
    return _read_from_env(
        property_name="base_url",
        env_name=CELONIS_URL_ENV,
        error_message=f"URL is needed to connect to EMS, either pass as argument 'base_url' or set environment "
        f"variables "
        f"'{CELONIS_URL_ENV}'.",
    )


def _read_api_token_from_env() -> str:
    return _read_from_env(
        property_name="api_token",
        env_name=CELONIS_API_TOKEN_ENV,
        error_message=f"""
            {CELONIS_API_TOKEN_ENV} is needed to connect to EMS, either pass as argument 'api_token'
            or set environment variable '{CELONIS_API_TOKEN_ENV}'.
            When using the ML Workbench the API token is set automatically.
            When using an Application Key: /help/display/CIBC/Application+Keys.
            """,
    )


def _read_key_type_from_env() -> typing.Optional[str]:
    try:
        return _read_from_env(
            property_name="key_type",
            env_name=CELONIS_KEY_TYPE_ENV,
        )
    except PyCelonisValueError:
        return None


def _read_from_env(property_name: str, env_name: str, error_message: typing.Optional[str] = None) -> str:
    value = os.environ.get(env_name)

    if not value:
        raise PyCelonisValueError(error_message or "")

    logger.info("No `%s` given. Using environment variable '%s'", property_name, env_name)
    return value


def _check_url(base_url: str) -> str:
    regex = r"^(https?://)?([^/]+)"
    result = re.search(regex, base_url)

    if not result:
        raise PyCelonisValueError(f"Invalid URL format: {base_url}")

    http = result[1] or "https://"
    base_url = http + result[2]
    return base_url


def _infer_client(
    base_url: str,
    api_token: APITokenType,
    key_type: typing.Union[str, KeyType, None],
    user_agent: str,
    proxies: typing.Optional[ProxyTypes],
    **kwargs: typing.Any,
) -> Client:
    if key_type:
        if isinstance(key_type, str):
            key_type = KeyType[key_type]
        key_type = typing.cast(KeyType, key_type)
        client = Client(
            base_url=base_url, api_token=api_token, key_type=key_type, user_agent=user_agent, proxy=proxies, **kwargs
        )
    else:
        client = _try_default_client(base_url, api_token, user_agent, proxies, **kwargs)

    return client


def _try_default_client(
    base_url: str,
    api_token: APITokenType,
    user_agent: str,
    proxies: typing.Optional[ProxyTypes],
    **kwargs: typing.Any,
) -> Client:
    try:
        client = Client(
            base_url=base_url,
            api_token=api_token,
            key_type=KeyType.APP_KEY,
            user_agent=user_agent,
            proxy=proxies,
            **kwargs,
        )
        TeamService.get_api_cloud(client)
        logger.warning("KeyType is not set. Defaulted to 'APP_KEY'.")
    except PyCelonisPermissionError:
        client = Client(
            base_url=base_url,
            api_token=api_token,
            key_type=KeyType.USER_KEY,
            user_agent=user_agent,
            proxy=proxies,
            **kwargs,
        )
        TeamService.get_api_cloud(client)
        logger.warning("KeyType is not set. Defaulted to 'USER_KEY'.")
    return client


def _check_if_outdated() -> None:
    latest_version = parse(_get_latest_version())
    current_version = parse(__version__)
    if latest_version > current_version:
        logger.warning(
            "Your PyCelonis Version %s is outdated (Newest Version: %s). "
            "Please upgrade the package via: "
            "pip install --extra-index-url=https://pypi.celonis.cloud/ pycelonis pycelonis_core --upgrade",
            __version__,
            latest_version,
        )


def _get_latest_version() -> str:
    try:
        response = httpx.get("https://pypi.celonis.cloud/pycelonis/")
        # RegEx below does the following: first brackets ensure to find the last match for the pattern
        # in the next brackets. Second group is pattern X.X.X.tar.gz
        result = re.search(r"(?s:.*)([0-9]+\.[0-9]+\.[0-9]+).tar.gz", response.text)
        if result is None:
            return __version__
        return result.group(1)
    except httpx.RequestError:
        return __version__


def _connect(client: Client) -> None:
    try:
        TeamService.get_api_cloud(client)
        logger.info("Initial connect successful! PyCelonis Version: %s", __version__)
    except PyCelonisPermissionError:
        logger.error(
            "Couldn't connect to Celonis EMS %s.\n"
            "Please check if you set the correct 'key_type' and the token is valid. "
            "To learn more about setting up your Application Key correctly, "
            "check out %s/help/display/CIBC/Application+Keys.",
            client.base_url,
            client.base_url,
        )


def _print_permissions(celonis: Celonis) -> None:
    permissions = celonis.team.get_permissions()
    for permission in permissions:
        if permission is not None:
            logger.info("`%s` permissions: %s", permission.service_name, permission.permissions)


def _is_tracking_disabled(celonis: Celonis) -> bool:
    try:
        return not celonis.team.get_team().tracking_enabled
    except PyCelonisError:
        return True

