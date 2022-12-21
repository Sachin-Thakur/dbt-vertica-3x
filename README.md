# dbt-vertica
Your [dbt](https://www.getdbt.com/) adapter for [Vertica](https://www.vertica.com/).
Uses [vertica-python](https://github.com/vertica/vertica-python) to connect to Vertica database.
## Supported Features
### dbt Core Features
Below is a table for what features the current Vertica adapter supports for dbt. This is constantly improving and changing as both dbt adds new functionality, as well as the dbt-vertica driver improves. This list is based upon dbt 1.3.0
| dbt Core Features                                 | Supported   |
| ------------------------------------------------- | ----------- |
| Table Materializations                            | Yes         |
| Ephemeral Materializations                        | Yes         |
| View Materializations                             | Yes         |
| Incremental Materializations - Append             | Yes         |
| Incremental Materailizations - Insert + Overwrite | Yes         |
| Incremental Materializations - Merge              | Yes         |
| Snapshots - Timestamp                             | Yes         |
| Snapshots - Check Cols                            | No Paritial |
| Seeds                                             | Yes         |
| Tests                                             | Yes         |
| Documentation                                     | Yes         |
| External Tables                                   | Untested    |
* **Yes** - Supported, and tests pass.
* **No** - Not supported or implemented.
* **Untested** - May support out of the box, though hasn't been tested.
* **Passes Test** -The testes have passed, though haven't tested in a production like environment
### Vertica Features
Below is a table for what features the current Vertica adapter supports for Vertica. This is constantly improving and changing as both dbt adds new functionality, as well as the dbt-vertica driver improves.
| Vertica Features      | Supported |    
| --------------------- | --------- |
| Created/Drop Schema   | Yes       |
| Analyze Statistics    | No        |
| Purge Delete Vectors  | No        |
| Projection Management | No        |
| Primary/Unique Keys   | No        |
| Other DDLs            | No        |
## Changes
### 1.3.0
- Python Models (if applicable)
- Incremental Materialization: cleanup and standardization
- More functional adapter tests to inherit
### 1.2.0
- migrate necessary cross-db macros into adapter and ensure they're tested accordingly 
- remove any copy-and-pasted materialization (if your adapter inherits from another adapter) 

- add new basic tests BaseDocsGenerate and BaseDocsGenReferences 

- consider checking and testing support for Python 3.10 

- dbt-labs/dbt-core#5432 might make it into the second release cut in the next week, in which case, you'll also might want to:implement method and tests for connection retry logic1.0.3 

- Refactored the adapter to model after dbt's global_project macros 

- Unimplemented functions should throw an exception that it's not implemented. If you stumble across this, please open an Issue or PR so we can investigate. 

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
## Install
```
pip install dbt-vertica
```
You don't need to install dbt separately. Installing `dbt-vertica` will also install `dbt-core` and `vertica-python`.
## Sample Profile Configuration
```yaml
your-profile:
  outputs:
    dev:
      type: vertica # Don't change this!
      host: vertica-host-name
      port: 5433 # or your custom port (optional)
      username: your-username
      password: your-password
      database: vertica-database-name
      schema: your-default-schema
      connection_load_balance: True
      backup_server_node: ['123.123.123.123','www.abc.com',('123.123.123.123',5433)]


  target: dev
```
By default, `dbt-vertica` will request `ConnectionLoadBalance=true` (which is generally a good thing), and set a session label of `dbt_your-username`.

Load Balancing– Connection Load Balancing helps automatically spread the overhead caused by client connections across the cluster by having hosts redirect client connections to other hosts. Both the server and the client need to enable load balancing for it to function. If the server disables connection load balancing, the load balancing request from client will be ignored. 

`connection_load_balance : True` this paramerter will enable the load balancing in vertica  and `connection_load_balance : False` will disable the  load balancing in vertica.

Backup Server Node– Supply a list of backup hosts to backup_server_node for the client to try if the primary host you specify in the connection parameters (host, port) is unreachable. Each item in the list should be either a host string (using default port 5433) or a (host, port) tuple. A host can be a host name or an IP address.
Format of  passing backup server node in profiles.yml is  below:

`backup_server_node: ['123.123.123.123','www.abc.com',('123.123.123.123',5433)]`



There are three options for SSL: `ssl`, `ssl_env_cafile`, and `ssl_uri`.
See their use in the code [here](https://github.com/mpcarter/dbt-vertica/blob/d15f925049dabd2833b4d88304edd216e3f654ed/dbt/adapters/vertica/connections.py#L72-L87).
## Reach out!
First off, I would not have been able to make this adapater if the smart folks at dbt labs didn't make it so easy. That said, it seems every database has its own little quirks. I ran into several different issues when adapting the macros to Vertica. If you find something not working right, please open an issue (assuming it has to do with the adapter and not dbt itself).
Also, I would be excited to hear about anyone who is able to benefit from using dbt with Vertica. (Just open an issue to leave me a comment.)
## Develop
Run a local Vertica instance like:
    docker run -p 5433:5433 \
               -p 5444:5444 \
               -e VERTICA_DB_NAME=docker \
               -e VMART_ETL_SCRIPT="" \
               -e VMART_ETL_SQL="" \
               vertica/vertica-ce
Access the local Vertica instance like:
    docker exec -it <docker_image_name> /opt/vertica/bin/vsql
You need the pytest dbt adapter:
    pip3 install pytest-dbt-adapter==0.6.0
Run tests via:
    pytest tests/integration.dbtspec
    # run an individual test with increased logging:
    pytest tests/integration.dbtspec::test_dbt_base -xs --ff