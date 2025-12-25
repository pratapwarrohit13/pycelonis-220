"""Module for knowledge model content."""
import logging
import typing

from pycelonis.ems.studio.content_node.knowledge_model.component import Filter, Record
from pycelonis.service.semantic_layer.service import (
    ActionMetadata,
    ActivityMetadata,
    AnomalyMetadata,
    BaseMetadata,
    EventLogMetadata,
    KpiMetadata,
    LayerKind,
    LayerMetadata,
    LayerTransport,
    VariableMetadata,
)
from pycelonis_core.base.collection import CelonisCollection
from pydantic.v1 import validator

logger = logging.getLogger(__name__)


class KnowledgeModelContent(LayerTransport):
    """Class for knowledge model content to read properties from knowledge model."""

    kind: typing.Optional["LayerKind"]
    metadata: typing.Optional["LayerMetadata"]
    kpis: typing.Optional[CelonisCollection[typing.Optional["KpiMetadata"]]]
    records: typing.Optional[CelonisCollection[typing.Optional[Record]]]  # type: ignore
    variables: typing.Optional[CelonisCollection[typing.Optional["VariableMetadata"]]]
    filters: typing.Optional[CelonisCollection[typing.Optional[Filter]]]  # type: ignore
    activities: typing.Optional[CelonisCollection[typing.Optional["ActivityMetadata"]]]
    actions: typing.Optional[CelonisCollection[typing.Optional["ActionMetadata"]]]
    anomalies: typing.Optional[CelonisCollection[typing.Optional["AnomalyMetadata"]]]
    event_logs: typing.Optional[CelonisCollection[typing.Optional["EventLogMetadata"]]]
    custom_objects: typing.Optional[CelonisCollection[typing.Optional["BaseMetadata"]]]

    # validators
    _collection_validators = validator(
        "kpis",
        "records",
        "variables",
        "filters",
        "activities",
        "actions",
        "anomalies",
        "event_logs",
        "custom_objects",
        allow_reuse=True,
    )(CelonisCollection.from_list)

    @classmethod
    def from_transport(cls, layer_transport: LayerTransport) -> "KnowledgeModelContent":
        """Creates high-level knowledge model content object from given LayerTransport.

        Args:
            layer_transport: LayerTransport object containing properties of knowledge model content.

        Returns:
            A KnowledgeModelContent object with properties from transport.
        """
        return cls(**layer_transport.dict())

    def __main_attributes__(self) -> typing.List[str]:
        return ["metadata", "kind"]

