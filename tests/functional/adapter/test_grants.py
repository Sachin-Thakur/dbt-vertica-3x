# import pytest
from dbt.tests.adapter.grants.base_grants import BaseGrants
from dbt.tests.adapter.grants.test_invalid_grants import BaseInvalidGrants

import pytest
from dbt.tests.util import (
    run_dbt_and_capture,
    write_file,
)

my_invalid_model_sql = """
  select 1 as fun
"""

invalid_user_table_model_schema_yml = """
version: 2
models:
  - name: my_invalid_model
    config:
      materialized: table
      grants:
        select: ['invalid_user']
"""

invalid_privilege_table_model_schema_yml = """
version: 2
models:
  - name: my_invalid_model
    config:
      materialized: table
      grants:
        fake_privilege: ["{{ env_var('DBT_TEST_USER_2') }}"]
"""


class BaseInvalidGrantsVertica(BaseGrants):

    def test_invalid_grants(self, project, get_test_users, logs_dir):
        
        # failure when grant to a user/role that doesn't exist
        yaml_file = self.interpolate_name_overrides(invalid_user_table_model_schema_yml)
        write_file(yaml_file, project.project_root, "models", "schema.yml")
        (results, log_output) = run_dbt_and_capture(["--debug", "run"])
        assert results,self.grantee_does_not_exist_error() in log_output

        # failure when grant to a privilege that doesn't exist
        yaml_file = self.interpolate_name_overrides(invalid_privilege_table_model_schema_yml)
        write_file(yaml_file, project.project_root, "models", "schema.yml")
        (results, log_output) = run_dbt_and_capture(["--debug", "run"])
        assert results,self.privilege_does_not_exist_error() in log_output

class TestInvalidGrantsVertica(BaseInvalidGrantsVertica,BaseInvalidGrants):
    pass

