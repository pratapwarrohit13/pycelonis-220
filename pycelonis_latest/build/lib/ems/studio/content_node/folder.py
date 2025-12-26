"""Module to interact with Folders.

This module contains class to interact with Folders in Studio.

Typical usage example:

    ```python
    folder = package.get_folder(ANALYSIS_ID)
    folder = package.create_folder("NEW_FOLDER")
    folder.delete()
    ```
"""
import logging

from pycelonis.ems.studio.content_node import ContentNode

logger = logging.getLogger(__name__)


class Folder(ContentNode):
    """Folder object to interact with folder specific studio endpoints."""

