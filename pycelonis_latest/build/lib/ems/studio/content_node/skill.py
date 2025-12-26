"""Module to interact with Skills.

This module contains class to interact with Skills in Studio.

Typical usage example:

    ```python
    skill = package.get_skill(SKILL_ID)
    skill.delete()
    ```
"""

from pycelonis.ems.studio.content_node import ContentNode


class Skill(ContentNode):
    """Skill object to interact with skill specific studio endpoints."""

