import pytest
from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_singular_tests_ephemeral import (
    BaseSingularTestsEphemeral,
)

from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_ephemeral import BaseEphemeral
from dbt.tests.adapter.basic.test_incremental import BaseIncremental,BaseIncrementalNotSchemaChange
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_adapter_methods import BaseAdapterMethod
from dbt.tests.adapter.basic.test_validate_connection import BaseValidateConnection
from dbt.tests.adapter.basic.test_docs_generate import BaseDocsGenerate
from dbt.tests.adapter.basic.expected_catalog import base_expected_catalog
from tests.functional.adapter.expected_stats import vertica_stats
from expected_stats import vertica_stats

class TestSingularTestsEphemeralVertica(BaseSingularTestsEphemeral):
    pass

class TestEmptyVertica(BaseEmpty):
    pass

class TestGenericTestsVertica(BaseGenericTests):
    pass

class TestBaseAdapterMethodVertica(BaseAdapterMethod):
    pass

class TestVerticaValidateConnection(BaseValidateConnection):
    pass


class TestSimpleMaterializationsVertica(BaseSimpleMaterializations):
    pass



class TestEphemeralVertica(BaseEphemeral):
    pass



class TestIncrementalVertica(BaseIncremental):
    pass


class TestBaseIncrementalNotSchemaChangeVertica(BaseIncrementalNotSchemaChange):
    pass

class TestSnapshotCheckColsVertica(BaseSnapshotCheckCols):
    pass


class TestSnapshotTimestampVertica(BaseSnapshotTimestamp):
    pass


# class TestDocsGenerateVertica(BaseDocsGenerate):
#     @pytest.fixture(scope="class")
#     def test_expected_catalog(self, project):
#         return base_expected_catalog(
#             project,
#             role=None,
#             id_type="INT64",
#             text_type="STRING",
#             time_type="DATETIME",
#             view_type="view",
#             table_type="table",
#             model_stats=vertica_stats(False),
#             seed_stats=vertica_stats(True),
#         )

#         # project,
#         #     role=None,
#         #     id_type="integer",
#         #     text_type="text",
#         #     time_type="timestamp without time zone",
#         #     view_type="VIEW",
#         #     table_type="BASE TABLE",
#         #     model_stats=vertica_stats(False),
#         #     seed_stats=vertica_stats(True),
#         # )

# from dbt.tests.adapter.ephemeral.test_ephemeral import TestEphemeralMulti
# class TestEphemeralMultiVertica(TestEphemeralMulti):
#     pass

