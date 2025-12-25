"""Module to interact with Action Flows.

This module contains class to interact with Action Flows in Studio.

Typical usage example:

    ```python
    action_flow = package.get_action_flow(ACTION_FLOW_ID)
    action_flow.delete()
    ```
"""

from pycelonis.ems.studio.content_node import ContentNode


class ActionFlow(ContentNode):
    """Action flow object to interact with action flow specific studio endpoints."""

