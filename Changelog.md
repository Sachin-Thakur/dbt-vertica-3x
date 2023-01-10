## Changelog
- This file provides a full account of all changes to dbt-vertica
- "Breaking changes" listed under a version may require action from end users.
### 1.3.0
#### Features:
- Python Models (if applicable)
- Incremental materialization refactor and cleanup
- More functional adapter tests to inherit
- Add reusable function for retrying adapter connections.
- Updated to support for Vertica’s Connection Load Balancing and Backup Server Node connection properties. 
- Support for incremental model strategy ‘Append’. 
- Support for incremental model strategy ‘insert_overwrite’.
- add new basic tests BaseDocsGenerate and BaseDocsGenReferences
- defined profile_template which helps user to config profile while creating the project.
#### Fixes:
- Updates to correctly handle errors for multi-statement queries.
- Support for multiple optimization parameters for table materialization. 
- Support for enabling privileges inheritance for tables/views using INCLUDE SCHEMA PRIVILEGES by default in model materialization like table and view. If not required, can be disabled using EXCLUDE in the Vertica Server.
- removed copy-and-pasted materialization.
- consider checking and testing support for Python 3.10 
#### Breaking Changes
#####  Change description:
- Support for dbt-core version 1.3.0 and current testing framework migrated to new testing framework according to DBT guidelines
- Refactored the existing functionality of merge and delete+insert.
##### impact:
- For the incremental model strategy like ‘delete+insert’ and ‘merge’, `unique_key` is a required parameter fails if not provided.
##### workaround/solution:
- when using the incremental model strategy like ‘delete+insert’ and ‘merge’ pass the required parameter `unique_key` in config.
### 1.0.3
- Refactored the adapter to model after dbt's global_project macros
- Unimplemented functions should throw an exception that it's not implemented. If you stumble across this, please open an Issue or PR so we can investigate.
### 1.0.2
- Added support for snapshot timestamp with passing tests
- Added support for snapshot check cols with passing tests
### 1.0.1
- Fixed the Incremental method implementation (was buggy/incomplete)
   - Removed the `unique_id` as it wasn't implemented
   - Fixed when no fields were added - full table merge
- Added testing for Incremental materialization
  - Testing for dbt Incremental full table
  - Testing for dbt Incremental specified merged columns
- Added more logging to the connector to help understand why tests were failing
- Using the official [Vertica CE 11.0.x docker image](https://hub.docker.com/r/vertica/vertica-ce) now for tests
### 1.0.0
- Add support for DBT version 1.0.0
### 0.21.1
- Add testing, fix schema drop.
### 0.21.0
- Add `unique_field` property on connection, supporting 0.21.x.
### 0.20.2
- Added SSL options.
### 0.20.1
- Added the required changes from dbt 0.19.0. [Details found here](https://docs.getdbt.com/docs/guides/migration-guide/upgrading-to-0-19-0#for-dbt-plugin-maintainers).
- Added support for the MERGE command for incremental loading isntead of DELETE+INSERT