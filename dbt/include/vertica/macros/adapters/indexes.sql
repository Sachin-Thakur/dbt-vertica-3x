
{# 
  No need to implement create_indexes(). Syntax supported by default. 
#}

{% macro get_create_index_sql(relation, index_dict) -%}
  {{ return(adapter.dispatch('get_create_index_sql', 'dbt')(relation, index_dict)) }}
{% endmacro %}

{% macro vertica__get_create_index_sql(relation, index_dict) -%}
  {% do return(None) %}
{% endmacro %}
