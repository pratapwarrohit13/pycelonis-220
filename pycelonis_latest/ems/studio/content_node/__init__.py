"""Module to interact with content nodes.

This module contains class to interact with a content node in EMS Studio.

Typical usage example:

    ```python
    package = space.get_package(package_id)
    folder = package.create_folder("FOLDER_NAME")
    package.get_folder(folder.id)
    package.publish(version="1.0.0")
    ```
"""
import enum
import logging
import typing

from pycelonis.ems.studio.content_node import content_node_factory
from pycelonis.service.package_manager.service import (
    ContentNodeTransport,
    ContentNodeType,
    PackageManagerService,
    SaveContentNodeTransport,
)
from pycelonis_core.client.client import Client
from pydantic.v1 import Field

logger = logging.getLogger(__name__)


class AssetType(enum.Enum):
    """Enum class for different asset types available within Studio."""

    ANALYSIS = "ANALYSIS"
    SEMANTIC_MODEL = "SEMANTIC_MODEL"
    SCENARIO = "SCENARIO"
    BOARD = "BOARD"
    SKILL = "SKILL"
    SIMULATION_ASSET = "simulation-asset"


class ContentNode(ContentNodeTransport):
    """Content node object to interact with content node specific studio endpoints."""

    client: Client = Field(..., exclude=True)
    id: str
    """Id of studio content node."""
    key: str
    """Key of studio content node."""
    space_id: str
    """Id of space where content node is located."""
    serialized_content: typing.Optional[str]
    """Serialized content of content node."""
    root_with_key: str

    @classmethod
    def from_transport(cls, client: Client, content_node_transport: ContentNodeTransport) -> "ContentNode":
        """Creates high-level content node object from given ContentNodeTransport.

        Args:
            client: Client to use to make API calls for given content node.
            content_node_transport: ContentNodeTransport object containing properties of content node.

        Returns:
            A ContentNode object with properties from transport and given client.
        """
        return content_node_factory.ContentNodeFactory.get_content_node(client, content_node_transport)

    def update(self) -> None:
        """Pushes local changes of content node to EMS and updates properties with response from EMS."""
        updated_content_node = PackageManagerService.put_api_nodes_id(
            self.client, self.id, SaveContentNodeTransport(**self.json_dict())
        )
        logger.info("Successfully updated content node with id '%s'", self.id)
        self._update(updated_content_node)

    def sync(self) -> None:
        """Syncs content node properties with EMS."""
        synced_content_node = PackageManagerService.get_api_nodes_id(self.client, self.id)
        self._update(synced_content_node)

    def delete(self) -> None:
        """Deletes content node."""
        PackageManagerService.delete_api_nodes_id(self.client, self.id)
        logger.info("Successfully deleted content node with id '%s'", self.id)

    def __main_attributes__(self) -> typing.Optional[typing.List[str]]:
        return ["id", "key", "name", "root_node_key", "space_id"]

    ############################################################
    # Content Node Type
    ############################################################
    @staticmethod
    def is_package(content_node_transport: "ContentNodeTransport") -> bool:
        """Returns whether content node transport is package.

        Args:
            content_node_transport: Content node transport to check.

        Returns:
            Boolean if transport is package.
        """
        return content_node_transport.node_type == ContentNodeType.PACKAGE

    @staticmethod
    def is_folder(content_node_transport: "ContentNodeTransport") -> bool:
        """Returns whether content node transport is package.

        Args:
            content_node_transport: Content node transport to check.

        Returns:
            Boolean if transport is folder.
        """
        return content_node_transport.node_type == ContentNodeType.FOLDER

    @staticmethod
    def is_analysis(content_node_transport: "ContentNodeTransport") -> bool:
        """Returns whether content node transport is analysis.

        Args:
            content_node_transport: Content node transport to check.

        Returns:
            Boolean if transport is analysis.
        """
        return (
            content_node_transport.node_type == ContentNodeType.ASSET
            and content_node_transport.asset_type == AssetType.ANALYSIS.value
        )

    @staticmethod
    def is_knowledge_model(content_node_transport: "ContentNodeTransport") -> bool:
        """Returns whether content node transport is knowledge model.

        Args:
            content_node_transport: Content node transport to check.

        Returns:
            Boolean if transport is knowledge model.
        """
        return (
            content_node_transport.node_type == ContentNodeType.ASSET
            and content_node_transport.asset_type == AssetType.SEMANTIC_MODEL.value
        )

    @staticmethod
    def is_action_flow(content_node_transport: "ContentNodeTransport") -> bool:
        """Returns whether content node transport is action flow.

        Args:
            content_node_transport: Content node transport to check.

        Returns:
            Boolean if transport is action flow.
        """
        return (
            content_node_transport.node_type == ContentNodeType.ASSET
            and content_node_transport.asset_type == AssetType.SCENARIO.value
        )

    @staticmethod
    def is_view(content_node_transport: "ContentNodeTransport") -> bool:
        """Returns whether content node transport is view.

        Args:
            content_node_transport: Content node transport to check.

        Returns:
            Boolean if transport is view.
        """
        return (
            content_node_transport.node_type == ContentNodeType.ASSET
            and content_node_transport.asset_type == AssetType.BOARD.value
        )

    @staticmethod
    def is_simulation(content_node_transport: "ContentNodeTransport") -> bool:
        """Returns whether content node transport is simulation.

        Args:
            content_node_transport: Content node transport to check.

        Returns:
            Boolean if transport is simulation.
        """
        return (
            content_node_transport.node_type == ContentNodeType.ASSET
            and content_node_transport.asset_type == AssetType.SIMULATION_ASSET.value
        )

    @staticmethod
    def is_skill(content_node_transport: "ContentNodeTransport") -> bool:
        """Returns whether content node transport is skill.

        Args:
            content_node_transport: Content node transport to check.

        Returns:
            Boolean if transport is skill.
        """
        return (
            content_node_transport.node_type == ContentNodeType.ASSET
            and content_node_transport.asset_type == AssetType.SKILL.value
        )

