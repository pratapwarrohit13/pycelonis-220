"""Module to interact with tasks.

This module contains class to interact with a task in EMS data integration.

Typical usage example:

    ```python
    task = data_job.create_task("TEST_TASK", TaskType.TRANSFORMATION, "TEST_DESCRIPTION")
    transformation = data_job.create_transformation("TEST_TRANSFORMATION")
    transformation.delete()
    ```
"""
import logging
import typing

from pycelonis.ems.data_integration.table_extraction import TableExtraction
from pycelonis.service.integration.service import (
    IntegrationService,
    TableExtractionTransport,
    TaskInstanceTransport,
    TaskType,
    TaskUpdate,
)
from pycelonis_core.base.collection import CelonisCollection
from pycelonis_core.client.client import Client
from pycelonis_core.utils.errors import PyCelonisNotFoundError, PyCelonisValueError
from pydantic.v1 import Field

logger = logging.getLogger(__name__)


class Task(TaskInstanceTransport):
    """Task object to interact with task specific data integration endpoints."""

    client: Client = Field(..., exclude=True)
    id: str
    """Id of task."""
    pool_id: str
    """Id of data pool where task is located."""
    job_id: str
    """Id of job where task is located."""
    task_id: str
    name: typing.Optional[str]
    """Name of task."""

    @classmethod
    def from_transport(cls, client: Client, task_instance_transport: TaskInstanceTransport) -> "Task":
        """Creates high-level task object from given TaskTransport.

        Args:
            client: Client to use to make API calls for given job.
            task_instance_transport: TaskInstanceTransport object containing properties of task.

        Returns:
            A Task object with properties from transport and given client.
        """
        if task_instance_transport.task_type == TaskType.TRANSFORMATION:
            return Transformation(client=client, **task_instance_transport.dict())
        if task_instance_transport.task_type == TaskType.EXTRACTION:
            return Extraction(client=client, **task_instance_transport.dict())
        return cls(client=client, **task_instance_transport.dict())

    @property
    def data_pool_id(self) -> str:
        """Returns id of data pool for given task.

        Returns:
            Id of data pool.
        """
        return self.pool_id

    @data_pool_id.setter
    def data_pool_id(self, data_pool_id: str) -> None:
        """Sets data pool id for given task.

        Args:
            data_pool_id: New data pool id.
        """
        self.pool_id = data_pool_id

    def update(self) -> None:
        """Pushes local changes of task to EMS and updates properties with response from EMS."""
        updated_task = IntegrationService.put_api_pools_pool_id_jobs_job_id_tasks_task_instance_id(
            self.client,
            self.data_pool_id,
            self.job_id,
            self.id,
            TaskUpdate(**self.dict()),
        )
        logger.info("Successfully updated task with id '%s'", self.id)
        self._update(updated_task)

    def sync(self) -> None:
        """Syncs task properties with EMS."""
        for task in IntegrationService.get_api_pools_pool_id_jobs_job_id_tasks(
            self.client, self.data_pool_id, self.job_id
        ):
            if task is not None and task.id == self.id:
                self._update(task)
                return

        raise PyCelonisNotFoundError(f"Task with id '{self.id}' no longer exists.")

    def delete(self) -> None:
        """Deletes task."""
        IntegrationService.delete_api_pools_pool_id_jobs_job_id_tasks_task_instance_id(
            self.client, self.data_pool_id, self.job_id, self.id
        )
        logger.info("Successfully deleted task with id '%s'", self.id)

    def __main_attributes__(self) -> typing.Optional[typing.List[str]]:
        return [
            "id",
            "name",
            "disabled",
            "job_id",
            "pool_id",
            "task_id",
            "task_type",
        ]

    def enable(self) -> None:
        """Enables task."""
        IntegrationService.post_api_pools_pool_id_jobs_job_id_tasks_task_instance_id_enabled(
            self.client, self.data_pool_id, self.job_id, self.id
        )
        logger.info("Successfully enabled task with id '%s'", self.id)

    def disable(self) -> None:
        """Disables task."""
        IntegrationService.delete_api_pools_pool_id_jobs_job_id_tasks_task_instance_id_enabled(
            self.client, self.data_pool_id, self.job_id, self.id
        )
        logger.info("Successfully disabled task with id '%s'", self.id)


class Extraction(Task):
    """Extraction object to interact with extraction specific data integration endpoints."""

    client: Client = Field(..., exclude=True)
    id: str
    """Id of extraction."""
    pool_id: str
    """Id of data pool where extraction is located."""
    job_id: str
    """Id of job where extraction is located."""
    task_id: str

    def create_table_extraction(
        self,
        table_name: str,
        schema_name: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "TableExtraction":
        """Creates table extraction in given data job.

        Args:
            table_name: Name of table to extract.
            schema_name: Name of schema where table is located.
            **kwargs: Additional parameters set for
                [TableExtractionTransport][pycelonis.service.integration.service.TableExtractionTransport] object.

        Returns:
            A TableExtraction object for newly created table extraction.

        Raises:
            PyCelonisValueError: Raised if something went wrong creating the table extraction.
        """
        # Need to be empty lists instead of None to prevent null pointers
        connector_specific_configuration = kwargs.get("connector_specific_configuration", [])
        calculated_columns = kwargs.get("calculated_columns", [])

        table_extraction_transports = (
            IntegrationService.post_api_pools_pool_id_jobs_job_id_extractions_extraction_id_tables(
                self.client,
                self.data_pool_id,
                self.job_id,
                self.id,
                [
                    TableExtractionTransport(
                        table_name=table_name,
                        schema_name=schema_name,
                        task_id=self.task_id,
                        job_id=self.job_id,
                        connector_specific_configuration=connector_specific_configuration,
                        calculated_columns=calculated_columns,
                        **kwargs,
                    )
                ],
            )
        )

        if len(table_extraction_transports) != 1 or table_extraction_transports[0] is None:
            raise PyCelonisValueError("Something went wrong while creating the table extraction.")

        logger.info("Successfully created table extraction with id '%s'", table_extraction_transports[0].id)

        return TableExtraction.from_transport(
            self.client, self.data_pool_id, self.job_id, self.id, table_extraction_transports[0]
        )

    def get_table_extraction(self, id_: str) -> "TableExtraction":
        """Gets table extraction with given id.

        Args:
            id_: Id of table extraction.

        Returns:
            A TableExtraction object for table extraction with given id.
        """
        table_extraction_transport = (
            IntegrationService.get_api_pools_pool_id_jobs_job_id_extractions_extraction_id_tables_table_id(
                self.client, self.data_pool_id, self.job_id, self.id, id_
            )
        )
        return TableExtraction.from_transport(
            self.client, self.data_pool_id, self.job_id, self.id, table_extraction_transport
        )

    def get_table_extractions(self) -> "CelonisCollection[typing.Optional[TableExtraction]]":
        """Gets all table extractions of given data job.

        Returns:
            A list containing all table extractions.
        """
        table_extraction_transports = (
            IntegrationService.get_api_pools_pool_id_jobs_job_id_extractions_extraction_id_expanded(
                self.client, self.data_pool_id, self.job_id, self.id
            ).tables
        )
        return CelonisCollection(
            TableExtraction.from_transport(
                self.client, self.data_pool_id, self.job_id, self.id, table_extraction_transport
            )
            for table_extraction_transport in table_extraction_transports or []
            if table_extraction_transport is not None
        )


class Transformation(Task):
    """Transformation object to interact with transformation specific data integration endpoints."""

    def get_statement(self) -> typing.Optional[str]:
        """Gets statement of task."""
        return IntegrationService.get_api_pools_pool_id_jobs_job_id_transformations_transformation_id_statement(
            self.client, self.data_pool_id, self.job_id, self.id
        ).statement

    def update_statement(self, statement: str) -> None:
        """Updates statement of task.

        Args:
            statement: new statement of task.
        """
        IntegrationService.put_api_pools_pool_id_jobs_job_id_transformations_transformation_id_statement(
            self.client, self.data_pool_id, self.job_id, self.id, statement
        )
        logger.info("Successfully updated statement of task with id '%s'", self.id)

