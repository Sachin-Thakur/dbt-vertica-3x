import pytest

from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_singular_tests_ephemeral import (
    BaseSingularTestsEphemeral,
)
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_ephemeral import BaseEphemeral
from dbt.tests.adapter.basic.test_incremental import BaseIncremental
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_adapter_methods import BaseAdapterMethod
from dbt.tests.adapter.basic.test_validate_connection import BaseValidateConnection
from dbt.tests.adapter.basic.test_docs_generate import BaseDocsGenerate
from dbt.tests.adapter.basic.expected_catalog import base_expected_catalog
# from tests.functional.adapter.expected_stats import vertica_stats
from expected_stats import vertica_stats


class TestSimpleMaterializationsVertica(BaseSimpleMaterializations):
    pass

# class TestSimpleMaterializationsVertica(BaseSimpleMaterializations):
#     # This test requires a full-refresh to replace a table with a view
#     @pytest.fixture(scope="class")
#     def test_config(self):
#         return {"require_full_refresh": True}
from dbt.tests.adapter.basic.files import seeds_base_csv, seeds_added_csv, seeds_newcolumns_csv
schema_seed_added_yml = """
version: 2
seeds:
  - name: added
    config:
      column_types:
        name: varchar(64)
"""


class TestSingularTestsVertica(BaseSingularTests):
    # @pytest.fixture(scope="class")
    # def models(self):
    #     return {
    #         "base.csv": seeds_base_csv,
    #         "added.csv": seeds_added_csv,
    #         "seeds.yml": schema_seed_added_yml,
    #     }
    pass


class TestSingularTestsEphemeralVertica(BaseSingularTestsEphemeral):
    pass


class TestEmptyVertica(BaseEmpty):
    pass


class TestEphemeralVertica(BaseEphemeral):
    pass


class TestIncrementalVertica(BaseIncremental):
    pass


class TestGenericTestsVertica(BaseGenericTests):
    pass


class TestSnapshotCheckColsVertica(BaseSnapshotCheckCols):
    pass


class TestSnapshotTimestampVertica(BaseSnapshotTimestamp):
    pass


class TestBaseAdapterMethodVertica(BaseAdapterMethod):
    pass


class TestVerticaValidateConnection(BaseValidateConnection):
    pass


class TestDocsGenerateVertica(BaseDocsGenerate):
    @pytest.fixture(scope="class")
    def test_expected_catalog(self, project="vertica_profile_3x"):
        return base_expected_catalog(
            project='vertica_profile_3x',
            # role=None,
            # id_type="INT64",
            # text_type="STRING",
            # time_type="DATETIME",
            # view_type="view",
            # table_type="table",
            # model_stats=vertica_stats(False),
            # seed_stats=vertica_stats(True),
        )