from dbt.adapters.sql import SQLAdapter
from dbt.adapters.vertica import verticaConnectionManager

from dbt.adapters.base import available

import agate

class verticaAdapter(SQLAdapter):
    ConnectionManager = verticaConnectionManager

    @classmethod
    def date_function(cls):
        return 'sysdate'

   

    @classmethod
    def convert_text_type(cls, agate_table, col_idx):
        column = agate_table.columns[col_idx]
        lens = [len(d.encode("utf-8")) for d in column.values_without_nulls()]
        max_len = max(lens)+10 if lens else 64
        return "varchar({})".format(max_len)

    @classmethod
    def convert_number_type(cls, agate_table, col_idx):
        decimals = agate_table.aggregate(agate.MaxPrecision(col_idx))
        return "numeric(18,{})".format(decimals) if decimals else "integer"

    @available
    def standardize_grants_dict(self, grants_table: agate.Table) -> dict:
        """
        :param grants_table: An agate table containing the query result of
            the SQL returned by get_show_grant_sql
        :return: A standardized dictionary matching the `grants` config
        :rtype: dict
        """
        grants_dict: Dict[str, List[str]] = {}
        for row in grants_table:
            grantee = row["grantee"]
            privilege = row["privilege_type"]
            if privilege in grants_dict.keys():
                grants_dict[privilege].append(grantee)
            else:
                grants_dict.update({privilege: [grantee]})
        return grants_dict

    
    