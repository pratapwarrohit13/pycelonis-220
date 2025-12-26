"""Module to interact with Analyses.

This module contains class to interact with Analyses in Apps.
"""
import typing

from pycelonis.ems.apps.content_node import PublishedContentNode
from pycelonis.ems.apps.content_node.analysis.content import AnalysisContent, AnalysisDocument, AnalysisDraft
from pycelonis.errors import PyCelonisQueryResolutionError
from pycelonis.pql import PQL
from pycelonis.service.integration.service import DataQuery, QueryEnvironment
from pycelonis.service.process_analytics.service import (
    DataCommand,
    DataCommandBatchRequest,
    DataCommandBatchTransport,
    ProcessAnalyticsService,
)
from pycelonis.utils.json import load_json


class PublishedAnalysis(PublishedContentNode):
    """Analysis object to interact with analysis specific apps endpoints."""

    def get_content(self) -> typing.Optional["AnalysisContent"]:
        """Returns content of analysis.

        Returns:
            Analysis content.

        Examples:
            Extract table from analysis content:
            ```python
            sheet = analysis.get_content().draft.document.sheets[0]
            olap_table = sheet.components.find("#{OLAP Table}", search_attribute="title")
            ```
        """
        if self.serialized_content is None:
            return None
        return AnalysisContent(**load_json(self.serialized_content))

    def resolve_query(self, query: PQL) -> typing.Tuple[DataQuery, typing.Optional[QueryEnvironment]]:
        """Returns Data Query and Query environment for an analysis.

        Use this method to resolve queries that are based on analysis KPIs and Variables.
        The returned DataQuery and QueryEnvironment can than be used to query data via
        [DataModel.export_data_frame][pycelonis.ems.data_integration.data_model.DataModel.export_data_frame].

        Args:
            query: PQL query to be resolved

        Returns:
            Returns Data Query and Query environment

        Examples:
            Resolving a query from an analysis component to extract the data from the data model:
            ```python
            sheet = analysis.get_content().draft.document.sheets[0]
            olap_table = sheet.components.find("#{OLAP Table}", search_attribute="title")
            query = olap_table.get_query()

            data_query, query_environment = analysis.resolve_query(query)
            df = data_model.export_data_frame(data_query, query_environment)
            ```
        """
        content = self.get_content() or AnalysisContent()
        draft = content.draft or AnalysisDraft()
        document = draft.document or AnalysisDocument()
        variables = document.variables or []

        data_command_batch_request = DataCommandBatchRequest(
            variables=variables,
            requests=[DataCommandBatchTransport(request=DataCommand(commands=[DataQuery(queries=query.queries)]))],
        )

        post_batch_query_transport = ProcessAnalyticsService.post_analysis_v2_api_analysis_analysis_id_data_command(
            self.client, self.id, data_command_batch_request
        )

        analysis_commands = post_batch_query_transport.analysis_commands or []
        if len(analysis_commands) != 1 or analysis_commands[0] is None:
            raise PyCelonisQueryResolutionError("More than one analysis command resolved")

        request = analysis_commands[0].request or DataCommand()
        commands = request.commands or []
        if len(commands) != 1 or commands[0] is None:
            raise PyCelonisQueryResolutionError("More than one analysis command resolved")

        if not post_batch_query_transport.query_environment:
            raise PyCelonisQueryResolutionError("No query environment resolved")

        return DataQuery(**commands[0].json_dict()), QueryEnvironment(
            **post_batch_query_transport.query_environment.json_dict()
        )

