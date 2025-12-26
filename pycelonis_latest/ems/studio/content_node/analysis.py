"""Module to interact with Analyses.

This module contains class to interact with Analyses in Studio.

Typical usage example:

    ```python
    analysis = package.get_analysis(ANALYSIS_ID)
    analysis = package.create_analysis("NEW_ANALYSIS", data_model_id)
    analysis.delete()
    ```
"""
import logging

from pycelonis.ems.studio.content_node import ContentNode

logger = logging.getLogger(__name__)


class Analysis(ContentNode):
    """Analysis object to interact with analysis specific studio endpoints."""

