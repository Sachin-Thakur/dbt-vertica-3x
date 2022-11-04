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
from dbt.tests.adapter.basic.test_docs_generate import BaseDocsGenerate,BaseDocsGenReferences

from dbt.tests.adapter.basic.expected_catalog import base_expected_catalog,expected_references_catalog
from tests.functional.adapter.expected_stats import vertica_stats
from expected_stats import vertica_stats


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

class TestSingularTestsEphemeralVertica(BaseSingularTestsEphemeral):
    pass

class TestEphemeralVertica(BaseEphemeral):
    pass



class TestIncrementalVertica(BaseIncremental):
    pass


class TestBaseIncrementalNotSchemaChangeVertica(BaseIncrementalNotSchemaChange):
    pass

@pytest.mark.skip_profile('vertica')
class TestSnapshotCheckColsVertica(BaseSnapshotCheckCols):
    pass

class TestSnapshotTimestampVertica(BaseSnapshotTimestamp):
    pass


class TestDocsGenerateVertica(BaseDocsGenerate):
    @pytest.fixture(scope="class")
    def expected_catalog(self, project):
        return base_expected_catalog(
            project,
            role=None,
            id_type=1,
            time_type="11/12/2022",
            view_type="VIEW",
            table_type="BASE TABLE",
            model_stats=vertica_stats(False),
            text_type= "abc",
        )

class TestDocsGenReferencesVertica(BaseDocsGenReferences):
    @pytest.fixture(scope="class")
    def expected_catalog(self, project):
        return expected_references_catalog(
            project,
            role=None,
            id_type=1,
            bigint_type=135481653441354138548413384135,
            time_type="11/12/2022",
            view_type="VIEW",
            table_type="BASE TABLE",
            model_stats=vertica_stats(False),
            text_type= "abc",
        )


