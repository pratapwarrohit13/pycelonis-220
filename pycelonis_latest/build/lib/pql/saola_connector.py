from typing import TYPE_CHECKING, List

import pandas as pd
from pycelonis.pql.pql_debugger import PQLDebugger
from pycelonis.pql.pql_parser import PQLParser
from pycelonis.service.pql_language.service import PqlQueryType
from saolapy.pql.base import PQL, PQLColumn, PQLFilter
from saolapy.saola_connector import SaolaConnector

if TYPE_CHECKING:
    from pycelonis.ems import DataModel


class DataModelSaolaConnector(SaolaConnector):
    """Data model saola connector."""

    def __init__(self, data_model: "DataModel"):
        self.data_model = data_model

    def _export_data(self, query: PQL) -> pd.DataFrame:
        """Exports given PQL as data frame."""
        return self.data_model.export_data_frame(query)

    def verify_query(self, query: PQL) -> None:
        """Verifies given query."""
        self._verify_columns(query.columns)
        self._verify_filters(query.filters)

    def convert_filter_to_expressions(self, filter_: PQLFilter) -> List[str]:
        """Converts given pql filter to conditional expressions.

        Args:
            filter_: PQL filter to convert.

        Returns:
            Conditional expressions resulting from pql filter.
        """
        return PQLParser.convert_filter_to_expressions(self.data_model.client, self.data_model.id, filter_.query)

    def _verify_columns(self, columns: List[PQLColumn]) -> None:
        for col in columns:
            error_messages = PQLDebugger.debug(
                self.data_model.client, self.data_model.id, col.query, PqlQueryType.DIMENSION
            )
            if error_messages:
                raise ValueError(f"Errors in column '{col.name}':\n\n" + "\n\n\n".join(error_messages))

    def _verify_filters(self, filters: List[PQLFilter]) -> None:
        for filter_ in filters:
            error_messages = PQLDebugger.debug(
                self.data_model.client, self.data_model.id, filter_.query, PqlQueryType.FILTER
            )
            if error_messages:
                raise ValueError("Errors in filter:\n\n" + "\n\n\n".join(error_messages))

