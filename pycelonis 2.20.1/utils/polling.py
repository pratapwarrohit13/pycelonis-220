"""Module to poll different functions.

This module contains function to poll for a specific outcome.

Typical usage example:

    ```python
    poll(wait_for=lambda: not is_reload_in_progress(), sleep=2)
    ```
"""
import time
import typing

import tqdm.auto as tqdm
from pycelonis.config import Config

T = typing.TypeVar("T")


def poll(
    target: typing.Callable[..., T],
    message: typing.Optional[typing.Callable[[T], str]] = None,
    wait_for: typing.Optional[typing.Callable[[T], bool]] = None,
    sleep: int = 5,
) -> None:
    """Polls `wait_for` callable until it returns True.

    Args:
        target: Callable to poll target.
        message: Callable that takes target return value as input and transforms it to string displayed in progress bar.
        wait_for: Callable that takes target return value as input and transforms it to boolean indicating whether
            polling is finished.
        sleep: Time duration to wait between pools.
    """
    pbar = tqdm.tqdm(disable=Config.DISABLE_TQDM)

    while True:
        try:
            pbar.update()
            current_target = target()

            if message:
                pbar.set_postfix_str(message(current_target))

            if (wait_for is not None and wait_for(current_target)) or (wait_for is None and current_target):
                pbar.close()
                return

            time.sleep(sleep)
        except Exception:
            if hasattr(pbar, "disp"):  # Only tqdm notebook has attribute disp
                pbar.disp(bar_style="danger")
            raise

