"""Module to interact with data pools.

This module contains class to interact with a data pool in EMS Data integration.

Typical usage example:

    ```python
    data_pool = celonis.data_integration.get_data_pool(data_pool_id)
    data_pool.name = "NEW_NAME"
    data_pool.update()
    data_pool.delete()
    ```
"""
import logging

import pandas as pd
from pycelonis.ems.data_integration.data_connection import DataConnection
from pycelonis.ems.data_integration.data_model import DataModel
from pycelonis.ems.data_integration.data_pool_table import DataPoolTable
from pycelonis.ems.data_integration.data_push_job import DataPushJob
from pycelonis.ems.data_integration.job import Job
from pycelonis.errors import PyCelonisTableAlreadyExistsError
from pycelonis.service.integration.service import ColumnTransport, DataModelTransport, DataPoolTransport
from pycelonis.service.integration.service import DataPushJob as DataPushJobBase
from pycelonis.service.integration.service import IntegrationService, JobTransport, JobType, PoolTable, TableTransport
from pycelonis_core.base.collection import CelonisCollection
from pycelonis_core.client.client import Client
from pycelonis_core.utils.errors import PyCelonisNotFoundError, PyCelonisValueError
from pydantic.v1 import Field, typing

logger = logging.getLogger(__name__)


class DataPool(DataPoolTransport):
    """Data pool object to interact with data pool specific data integration endpoints."""

    client: Client = Field(..., exclude=True)
    id: str
    """Id of data pool."""
    name: typing.Optional[str]
    """Name of data pool."""

    @classmethod
    def from_transport(cls, client: Client, data_pool_transport: DataPoolTransport) -> "DataPool":
        """Creates high-level data pool object from given DataPoolTransport.

        Args:
            client: Client to use to make API calls for given data pool.
            data_pool_transport: DataPoolTransport object containing properties of data pool.

        Returns:
            A DataPool object with properties from transport and given client.
        """
        return cls(client=client, **data_pool_transport.dict())

    def update(self) -> None:
        """Pushes local changes of data pool to EMS and updates properties with response from EMS."""
        updated_data_pool = IntegrationService.put_api_pools_id(self.client, self.id, self)
        logger.info("Successfully updated data pool with id '%s'", self.id)
        self._update(updated_data_pool)

    def sync(self) -> None:
        """Syncs data pool properties with EMS."""
        synced_data_pool = IntegrationService.get_api_pools_id(self.client, self.id)
        self._update(synced_data_pool)

    def delete(self) -> None:
        """Deletes data pool."""
        IntegrationService.delete_api_pools_id(self.client, self.id)
        logger.info("Successfully deleted data pool with id '%s'", self.id)

    def __main_attributes__(self) -> typing.Optional[typing.List[str]]:
        return ["id", "name"]

    ############################################################
    # Data Model
    ############################################################
    def create_data_model(self, name: str, **kwargs: typing.Any) -> "DataModel":
        """Creates new data model with name in given data pool.

        Args:
            name: Name of new data model.
            **kwargs: Additional parameters set for
                [DataModelTransport][pycelonis.service.integration.service.DataModelTransport] object.

        Returns:
            A DataModel object for newly created data model.

        Examples:
            Create a data model and add tables:
            ```python
            data_model = data_pool.create_data_model("TEST_DATA_MODEL")
            data_model.add_table(name="ACTIVITIES", alias="ACTIVITIES")
            data_model.add_table(name="EKPO", alias="EKPO")
            ```
        """
        data_model_transport = IntegrationService.post_api_pools_pool_id_data_models(
            self.client, self.id, DataModelTransport(name=name, **kwargs)
        )
        logger.info("Successfully created data model with id '%s'", data_model_transport.id)
        return DataModel.from_transport(self.client, data_model_transport)

    def get_data_model(self, id_: str) -> "DataModel":
        """Gets data model with given id.

        Args:
            id_: Id of data model.

        Returns:
            A DataModel object for data model with given id.
        """
        data_model_transport = IntegrationService.get_api_pools_pool_id_data_models_data_model_id(
            self.client, self.id, id_
        )
        return DataModel.from_transport(self.client, data_model_transport)

    def get_data_models(self) -> CelonisCollection["DataModel"]:
        """Gets all data models of given data pool.

        Returns:
            A list containing all data models.
        """
        data_model_transports = IntegrationService.get_api_pools_pool_id_data_models(self.client, self.id)
        return CelonisCollection(
            DataModel.from_transport(self.client, data_model_transport)
            for data_model_transport in data_model_transports
            if data_model_transport is not None
        )

    ############################################################
    # Data Push Job
    ############################################################
    @staticmethod
    def create_data_push_job_from(
        client: Client,
        data_pool_id: str,
        target_name: str,
        type_: typing.Optional[JobType] = None,
        column_config: typing.Optional[typing.List[ColumnTransport]] = None,
        keys: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any,
    ) -> "DataPushJob":
        """Creates new data push job in given data pool.

        Args:
            client: Client to use to make API calls for data export.
            data_pool_id: Id of data pool where data push job will be created.
            target_name: Table name to which job will push data.
            type_: Type of data push job.
            column_config: Can be used to specify column types and string field length in number of characters.
            keys: Primary keys to use in case of upsert data push job.
            **kwargs: Additional parameters set for
                [DataPushJob][pycelonis.service.integration.service.DataPushJob] object.

        Returns:
            The newly created DataPushJob.

        Examples:
            Create data push job to replace table:
            ```python
            from pycelonis.ems import DataPool

            data_push_job = DataPool.create_data_push_job_from(
                client=celonis.client,
                data_pool_id="<data_pool_id>",
                target_name="ACTIVITIES",
                type_=JobType.REPLACE
            )

            with open("ACTIVITIES.parquet", "rb") as file:
                data_push_job.add_file_chunk(file)

            data_push_job.execute()
            ```
        """
        data_pool = DataPool(client=client, id=data_pool_id)
        return data_pool.create_data_push_job(
            target_name=target_name, type_=type_, column_config=column_config, keys=keys, **kwargs
        )

    def create_data_push_job(
        self,
        target_name: str,
        type_: typing.Optional[JobType] = None,
        column_config: typing.Optional[typing.List[ColumnTransport]] = None,
        keys: typing.Optional[typing.List[str]] = None,
        connection_id: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "DataPushJob":
        """Creates new data push job in given data pool.

        Args:
            target_name: Table name to which job will push data.
            type_: Type of data push job.
            column_config: Can be used to specify column types and string field length in number of characters.
            keys: Primary keys to use in case of upsert data push job.
            connection_id: Connection id of connection for data push job (Equivalent to data_source_id for pool tables).
            **kwargs: Additional parameters set for
                [DataPushJob][pycelonis.service.integration.service.DataPushJob] object.

        Returns:
            A DataPushJob object for newly created data push job.

        Examples:
            Create data push job to replace table:
            ```python
            data_push_job = data_pool.create_data_push_job(
                target_name="ACTIVITIES",
                type_=JobType.REPLACE
            )

            with open("ACTIVITIES.parquet", "rb") as file:
                data_push_job.add_file_chunk(file)

            data_push_job.execute()
            ```
        """
        table_schema = None if column_config is None else TableTransport(table_name=target_name, columns=column_config)

        data_push_job_transport = IntegrationService.post_api_v1_data_push_pool_id_jobs(
            self.client,
            self.id,
            DataPushJobBase(
                target_name=target_name,
                data_pool_id=self.id,
                table_schema=table_schema,
                type_=type_,
                keys=keys,
                connection_id=connection_id,
                **kwargs,
            ),
        )
        logger.info("Successfully created data push job with id '%s'", data_push_job_transport.id)
        return DataPushJob.from_transport(self.client, data_push_job_transport)

    def get_data_push_job(self, id_: str) -> "DataPushJob":
        """Gets data push job with given id.

        Args:
            id_: Id of data push job.

        Returns:
            A DataPushJob object for data push job with given id.
        """
        data_push_job_transport = IntegrationService.get_api_v1_data_push_pool_id_jobs_id(self.client, self.id, id_)
        return DataPushJob.from_transport(self.client, data_push_job_transport)

    def get_data_push_jobs(self) -> CelonisCollection["DataPushJob"]:
        """Gets all data push jobs of given data pool.

        Returns:
            A list containing all data push jobs.
        """
        data_push_job_transports = IntegrationService.get_api_v1_data_push_pool_id_jobs(self.client, self.id)
        return CelonisCollection(
            DataPushJob.from_transport(self.client, data_push_job_transport)
            for data_push_job_transport in data_push_job_transports
            if data_push_job_transport is not None
        )

    ############################################################
    # Data Pool Tables
    ############################################################
    def create_table(
        self,
        df: pd.DataFrame,
        table_name: str,
        drop_if_exists: bool = False,
        column_config: typing.Optional[typing.List[ColumnTransport]] = None,
        chunk_size: int = 100_000,
        force: bool = False,
        data_source_id: typing.Optional[str] = None,
        index: typing.Optional[bool] = False,
        **kwargs: typing.Any,
    ) -> "DataPoolTable":
        """Creates new table in given data pool.

        Args:
            df: DataFrame to push to new table.
            table_name: Name of new table.
            drop_if_exists: If true, drops existing table if it exists. If false, raises
                PyCelonisTableAlreadyExistsError if table already exists.
            column_config: Can be used to specify column types and string field length in number of characters.
            chunk_size: Number of rows to push in one chunk.
            force: If true, replacing table without column config is possible. Otherwise, error is raised if table would
                be replaced without column config.
            data_source_id: Id of data connection where table will be created (Equivalent to connection_id for data push
                jobs).
            index: Whether index is included in parquet file that is pushed. Default False. See
                [pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html).
            **kwargs: Additional parameters set for
                [DataPushJob][pycelonis.service.integration.service.DataPushJob] object.

        Returns:
            The new table object.

        Raises:
            PyCelonisTableAlreadyExistsError: Raised if drop_if_exists=False and table already exists.
            PyCelonisDataPushExecutionFailedError: Raised when table creation fails.
            PyCelonisValueError: Raised when table already exists and no column config is given.

        Examples:
            Create new table:
            ```python
            df = pd.DataFrame({"TEST_COLUMN": [1,2, 3]})

            pool_table = data_pool.create_table(df, "TEST_TABLE")
            ```
            Replace table:
            ```python
            from pycelonis.ems import ColumnTransport, ColumnType

            df = pd.DataFrame({"TEST_COLUMN": [1,2, 3]})
            column_config = [ColumnTransport(column_name="TEST_COLUMN", column_type=ColumnType.INTEGER)]
            pool_table = data_pool.create_table(
                df, "TEST_TABLE", drop_if_exists=True, column_config=column_config)
            ```
        """
        if self._table_is_in_data_pool(table_name):
            if not drop_if_exists:
                raise PyCelonisTableAlreadyExistsError(table_name)
            if column_config is None and not force:
                raise PyCelonisValueError(
                    f"Replacing table '{table_name}' without specifying column_config resets table schema to default. "
                    f"Especially STRING columns are affected where the default data type is VARCHAR(80) which causes"
                    f" longer strings to be cut at 80 characters. Either specify column_config or set `force=True`."
                )

        if column_config is None:
            logger.warning(
                "STRING columns are by default stored as VARCHAR(80) and therefore cut after 80 characters. You can "
                "specify a custom field length for each column using the `column_config` parameter."
            )

        data_push_job = self.create_data_push_job(
            target_name=table_name,
            type_=JobType.REPLACE,
            column_config=column_config,
            connection_id=data_source_id,
            **kwargs,
        )
        try:
            data_push_job.add_data_frame(df, chunk_size=chunk_size, index=index)
            data_push_job.execute()
            logger.info("Successfully created table '%s' in data pool", table_name)
        finally:
            data_push_job.delete()

        return self.get_table(table_name, data_source_id)

    def get_table(self, name: str, data_source_id: typing.Optional[str] = None) -> "DataPoolTable":
        """Gets table located in data pool with given name and data source id.

        Args:
            name: Name of table.
            data_source_id: Id of data connection where table is located (Equivalent to connection_id for data push
                jobs).

        Returns:
            The table object by name and data source id.

        Raises:
            PyCelonisNotFoundError: Raised if no table with name and data source id exists in given package.
        """
        for table in IntegrationService.get_api_pools_id_tables(self.client, self.id):
            if table is not None and table.name == name and table.data_source_id == data_source_id:
                return DataPoolTable.from_transport(self.client, self.id, table)

        raise PyCelonisNotFoundError(
            f"No data pool tables with name '{name}' and data source id {data_source_id} found in pool."
        )

    def get_tables(self) -> CelonisCollection[PoolTable]:
        """Gets all data pool tables of given data pool.

        Returns:
            A list containing all data pool tables.
        """
        return CelonisCollection(
            DataPoolTable.from_transport(self.client, self.id, table)
            for table in IntegrationService.get_api_pools_id_tables(self.client, self.id)
            if table is not None
        )

    def _table_is_in_data_pool(self, table_name: str) -> bool:
        return table_name in [table.name for table in self.get_tables()]

    ############################################################
    # Data Connection
    ############################################################
    def get_data_connection(self, id_: str) -> "DataConnection":
        """Gets data connection with given id.

        Args:
            id_: Id of data connection.

        Returns:
            A DataConnection object for data connection with given id.
        """
        data_source_transport = IntegrationService.get_api_pools_pool_id_data_sources_data_source_id(
            self.client, self.id, id_
        )
        return DataConnection.from_transport(self.client, data_source_transport)

    def get_data_connections(self) -> "CelonisCollection[DataConnection]":
        """Gets all data connections of given data pool.

        Returns:
            A list containing all data connections.
        """
        data_source_transports = IntegrationService.get_api_pools_pool_id_data_sources(self.client, self.id)
        return CelonisCollection(
            DataConnection.from_transport(self.client, data_source_transport)
            for data_source_transport in data_source_transports
            if data_source_transport is not None
        )

    ############################################################
    # Job
    ############################################################
    def create_job(self, name: str, data_source_id: typing.Optional[str] = None, **kwargs: typing.Any) -> "Job":
        r"""Creates new job with name in given data pool.

        Args:
            name: Name of new job.
            data_source_id: Data connection id to use for job scope. (Equivalent to connection_id for data push jobs).

        Returns:
            A Job object for newly created job.

        Examples:
            Create data job with transformation statement and execute it:
            ```python
            data_job = data_pool.create_job("PyCelonis Tutorial Job")

            task = data_job.create_transformation(
                name="PyCelonis Tutorial Task",
                description="This is an example task"
            )

            task.update_statement(\"\"\"
                DROP TABLE IF EXISTS ACTIVITIES;
                CREATE TABLE ACTIVITIES (
                    _CASE_KEY VARCHAR(100),
                    ACTIVITY_EN VARCHAR(300)
                );
            \"\"\")

            data_job.execute()
            ```
        """
        job_transport = IntegrationService.post_api_pools_pool_id_jobs(
            self.client,
            self.id,
            JobTransport(name=name, data_pool_id=self.id, data_source_id=data_source_id, **kwargs),
        )
        logger.info("Successfully created job with id '%s'", job_transport.id)
        return Job.from_transport(self.client, job_transport)

    def get_job(self, id_: str) -> "Job":
        """Gets job with given id.

        Args:
            id_: Id of job.

        Returns:
            A Job object for job with given id.
        """
        job_transport = IntegrationService.get_api_pools_pool_id_jobs_id(self.client, self.id, id_)
        return Job.from_transport(self.client, job_transport)

    def get_jobs(self) -> CelonisCollection["Job"]:
        """Gets all jobs of given data pool.

        Returns:
            A list containing all jobs.
        """
        job_transports = IntegrationService.get_api_pools_pool_id_jobs(self.client, self.id)
        return CelonisCollection(
            Job.from_transport(self.client, job_transport)
            for job_transport in job_transports
            if job_transport is not None
        )

