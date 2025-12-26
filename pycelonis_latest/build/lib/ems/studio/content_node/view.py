"""Module to interact with Views.

This module contains class to interact with Views in Studio.

Typical usage example:

    ```python
    view = package.get_view(SKILL_ID)
    view.delete()
    ```
"""

from pycelonis.ems.studio.content_node import ContentNode


class View(ContentNode):
    """View object to interact with view specific studio endpoints."""

