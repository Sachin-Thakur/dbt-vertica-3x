{% macro get_version() %}

  {% do log("The installed version of dbt-vertica is: " ~ dbt_version, info=true) %}

{% endmacro %}