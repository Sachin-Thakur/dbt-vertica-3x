from dbt.adapters.sql import SQLAdapter
from dbt.adapters.vertica import verticaConnectionManager
from dataclasses import dataclass
import agate
from dbt.adapters.base import (
    BaseAdapter,
    available,
    RelationType,
    SchemaSearchMap,
    AdapterConfig,
    PythonJobHelper,
)

from dbt.exceptions import (
 
    RuntimeException,
)



from typing import Dict, List, Optional, Any, Set, Union, Type
from dbt.adapters.base.relation import BaseRelation

@dataclass
class VerticaConfig(AdapterConfig):
    cluster_by: Optional[Union[List[str], str]] = None
    partition_by: Optional[Dict[str, Any]] = None
    kms_key_name: Optional[str] = None
    labels: Optional[Dict[str, str]] = None
    partitions: Optional[List[str]] = None
    grant_access_to: Optional[List[Dict[str, str]]] = None
    hours_to_expiration: Optional[int] = None
    require_partition_filter: Optional[bool] = None
    partition_expiration_days: Optional[int] = None
    merge_update_columns: Optional[str] = None

    
class verticaAdapter(SQLAdapter):
    ConnectionManager = verticaConnectionManager

    # @classmethod
    # def date_function(cls):
    #     return 'sysdate'

    @classmethod
    def date_function(cls):
        return 'datenow()'

    @classmethod
    def convert_text_type(cls, agate_table, col_idx):
        column = agate_table.columns[col_idx]
        lens = [len(d.encode("utf-8")) for d in column.values_without_nulls()]
        max_len = max(lens) if lens else 64
        return "varchar({})".format(max_len)

    @classmethod
    def convert_number_type(cls, agate_table, col_idx):
        decimals = agate_table.aggregate(agate.MaxPrecision(col_idx))
        return "numeric(18,{})".format(decimals) if decimals else "integer"

    def drop_schema(self, relation: BaseRelation):
        relations = self.list_relations(
            database=relation.database,
            schema=relation.schema
        )
        for relation in relations:
            self.drop_relation(relation)
        super().drop_schema(relation)



    # def valid_incremental_strategies(self):
    #     """The set of standard builtin strategies which this adapter supports out-of-the-box.
    #     Not used to validate custom strategies defined by end users.
    #     """
    #     return ["append", "delete+insert"]

    def valid_incremental_strategies(self):
        """The set of standard builtin strategies which this adapter supports out-of-the-box.
        Not used to validate custom strategies defined by end users.
        """
        return ["append"]

    def builtin_incremental_strategies(self):
        return ["append", "delete+insert", "merge", "insert_overwrite"]

    @available.parse_none
    def get_incremental_strategy_macro(self, model_context, strategy: str):
        # Construct macro_name from strategy name
        if strategy is None:
            strategy = "default"

        # validate strategies for this adapter
        valid_strategies = self.valid_incremental_strategies()
        valid_strategies.append("default")
        builtin_strategies = self.builtin_incremental_strategies()
        if strategy in builtin_strategies and strategy not in valid_strategies:
            raise RuntimeException(
                f"The incremental strategy '{strategy}' is not valid for this adapter"
            )

        strategy = strategy.replace("+", "_")
        macro_name = f"get_incremental_{strategy}_sql"
        # The model_context should have MacroGenerator callable objects for all macros
        if macro_name not in model_context:
            raise RuntimeException(
                'dbt could not find an incremental strategy macro with the name "{}" in {}'.format(
                    macro_name, self.config.project_name
                )
            )

        # This returns a callable macro
        return model_context[macro_name]


