# dbt-vertica
[dbt](https://www.getdbt.com/) adapter for [Vertica](https://www.vertica.com/) uses [vertica-python](https://github.com/vertica/vertica-python) to connect to your Vertica database.

For more information on using dbt with Vertica, consult the Vertica Setup and Configuration pages.

## Supported Features
### dbt Core Features
Below is a table for what features the current Vertica adapter supports for dbt. This is constantly improving and changing as both dbt adds new functionality, as well as the dbt-vertica driver improves. This list is based upon dbt 1.3.0
|                dbt Core Features                  | Supported   |
| ------------------------------------------------- | ----------- |
| Table Materializations                            | Yes         |
| Ephemeral Materializations                        | Yes         |
| View Materializations                             | Yes         |
| Incremental Materializations - Append             | Yes         |
| Incremental Materailizations - Merge              | Yes         |
| Incremental Materializations - Delete+Insert      | Yes         |
| Incremental Materializations - Insert_Overwrite   | Yes         |
| Snapshots - Timestamp                             | Yes         |
| Snapshots - Check Cols                            | No  |
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
|   Vertica Features    | Supported |    
| --------------------- | --------- |
| Created/Drop Schema   | Yes       |
| Analyze Statistics    | No        |
| Purge Delete Vectors  | No        |
| Projection Management | No        |
| Primary/Unique Keys   | No        |
| Other DDLs            | No        |

## Installation
```
$ pip install dbt-vertica
```
You don't need to install dbt separately. Installing `dbt-vertica` will also install `dbt-core` and `vertica-python`.
## Sample Profile Configuration
```profiles.yml

your-profile:
  outputs:
    dev:
      type: vertica # Don't change this!
      host: [hostname]
      port: [port] # or your custom port (optional)
      username: [your username] 
      password: [your password] 
      database: [database name] 
      schema: [dbt schema] 
      connection_load_balance: True
      backup_server_node: [list of backup hostnames or IPs]
      retries: [1 or more]
      threads: [1 or more] 
  target: dev

```
### Description of Profile Fields:

| Property | Description | Required? | Default Value | Example |
| -------- | ----------- | --------- | ------------- | ------- |
|  type	   | The specific adapter to use. |	Yes	| None | vertica |
| host	| The host name or IP address of any active node in the Vertica Server. |	Yes |	None |	127.0.0.1 |
| port |	The port to use, default or custom. |	Yes	| 5433 | 5433 |
| username | The username to use to connect to the server. | Yes | None	| dbadmin |
| password | The password to use for authenticating to the server. | Yes | None | my_password |
| database | The name of the database running on the server. | Yes | None | my_db |
| schema | The schema to build models into. | No | None | VMart |
| connection_load_balance | A Boolean value that indicates whether the connection can be redirected to a host in the database other than host. | No | true | true |
| backup_server_node | List of hosts to connect to if the primary host specified in the connection (host, port) is unreachable. Each item in the list should be either a host string (using default port 5433) or a (host, port) tuple. A host can be a host name or an IP address. | No | none | ['123.123.123.123','www.abc.com',('123.123.123.124',5433)]
| retries | The retry times after an unsuccessful connection. | No | 1 | 3 |
| threads | The number of threads the dbt project will run on. | No | 1 | 3 |
| label | A session label to identify the connection. | No | An auto-generated label with format of: dbt_<username>	| dbt_dbadmin |

For more information on Vertica’s connection properties please refer to Vertica-Python Connection Properties.

There are three options for SSL: `ssl`, `ssl_env_cafile`, and `ssl_uri`.
See their use in the code [here](https://github.com/mpcarter/dbt-vertica/blob/d15f925049dabd2833b4d88304edd216e3f654ed/dbt/adapters/vertica/connections.py#L72-L87).


added `INCLUDE SCHEMA PRIVILEGES` as the default for views and table materializations and if not required then user can exclude it manually.
