import pytest

import os



# Import the standard functional fixtures as a plugin

# Note: fixtures with session scope need to be local

pytest_plugins = ["dbt.tests.fixtures.project"]


@pytest.fixture(scope="class")
def dbt_profile_target():
  return {
    "type": "vertica",
    "threads": 4,
    "host": "159.65.150.255",
    "port": int(os.getenv("VERTICA_TEST_PORT", 5433)),
    "username": os.getenv("VERTICA_TEST_USER", "dbadmin"),
    "password": os.getenv("VERTICA_TEST_PASS", ""),
    "database": os.getenv("VERTICA_TEST_DATABASE","VMart"),
  }

