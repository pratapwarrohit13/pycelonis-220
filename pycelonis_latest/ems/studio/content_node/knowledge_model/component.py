"""Module for knowledge model components."""
import typing

from pycelonis.pql import PQLColumn, PQLFilter
from pycelonis.service.semantic_layer.service import (
    AttributeMetadata,
    BusinessRecordMetadata,
    FilterMetadata,
    PqlBaseMetadata,
)
from pycelonis_core.base.collection import CelonisCollection
from pydantic.v1 import validator


class Attribute(AttributeMetadata):
    """Class for knowledge model record attributes."""

    def get_column(self) -> PQLColumn:
        """Returns query of attribute.

        Returns:
            PQLColumn with attribute query.

        Examples:
            Extract data based on PQLs from knowledge model:
            ```python
            from pycelonis.pql import PQL, PQLColumn

            record = knowledge_model.get_content().records.find_by_id('ACTIVITIES')
            attribute = record.attributes.find_by_id('ACTIVITY_EN')

            query = PQL() + attribute.get_column()

            data_query, query_environment = knowledge_model.resolve_query(query)
            df = data_model.export_data_frame(data_query, query_environment)
            ```
        """
        return PQLColumn(name=self.id, query=self.pql)


class Identifier(PqlBaseMetadata):
    """Class for knowledge model record identifiers."""

    def get_column(self) -> PQLColumn:
        """Returns query of identifier.

        Returns:
            PQLColumn with identifier query.

        Examples:
            Extract data based on PQLs from knowledge model:
            ```python
            from pycelonis.pql import PQL, PQLColumn

            record = knowledge_model.get_content().records.find_by_id('ACTIVITIES')
            identifier = record.identifier

            query = PQL() + identifier.get_column()

            data_query, query_environment = knowledge_model.resolve_query(query)
            df = data_model.export_data_frame(data_query, query_environment)
            ```
        """
        return PQLColumn(name=self.id, query=self.pql)


class Record(BusinessRecordMetadata):
    """Class for knowledge model records."""

    attributes: typing.Optional[CelonisCollection[Attribute]]  # type: ignore
    identifier: typing.Optional[Identifier]

    # validators
    _record_validators = validator(
        "attributes",
        allow_reuse=True,
    )(CelonisCollection.from_list)


class Filter(FilterMetadata):
    """Class for knowledge model filters."""

    def get_filter(self) -> PQLFilter:
        """Returns query of filter.

        Returns:
            PQLColumn with filter query.

        Examples:
            Extract data based on PQLs from knowledge model:
            ```python
            from pycelonis.pql import PQL, PQLColumn

            km_filter = knowledge_model.get_content().filters.find_by_id('FILTER')

            query = PQL() + PQLColumn(name="<name>", query="<query>") + km_filter.get_filter()

            data_query, query_environment = knowledge_model.resolve_query(query)
            df = data_model.export_data_frame(data_query, query_environment)
            ```
        """
        return PQLFilter(query=self.pql)

