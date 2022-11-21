{% macro vertica__get_columns_in_relation(relation) -%}
  {% call statement('get_columns_in_relation', fetch_result=True) %}
    select
    column_name
    , data_type
    , character_maximum_length
    , numeric_precision
    , numeric_scale
    from (
        select
        column_name
        , data_type
        , character_maximum_length
        , numeric_precision
        , numeric_scale
        , ordinal_position
        from v_catalog.columns
        where table_schema = '{{ relation.schema }}'
        and table_name = '{{ relation.identifier }}'
        union all
        select
        column_name
        , data_type
        , character_maximum_length
        , numeric_precision
        , numeric_scale
        , ordinal_position
        from v_catalog.view_columns
        where table_schema = '{{ relation.schema }}'
        and table_name = '{{ relation.identifier }}'
    ) t
    order by ordinal_position
  {% endcall %}
  {% set table = load_result('get_columns_in_relation').table %}
  {{ return(sql_convert_columns_in_relation(table)) }}
{% endmacro %}


{% macro vertica__sql_convert_columns_in_relation(table) -%}
  {{ exceptions.raise_not_implemented(
    'sql_convert_columns_in_relation macro not implemented for adapter '+adapter.type()) }}
{%- endmacro %}



{% macro vertica__alter_column_type(relation, column_name, new_column_type) -%}
  {#
    1. Create a new column (w/ temp name and correct type)
    2. Copy data over to it
    3. Drop the existing column (cascade!)
    4. Rename the new column to existing column
  #}
  {%- set tmp_column = column_name + "__dbt_alter" -%}

  {% call statement('alter_column_type') %}
    alter table {{ relation }} add column {{ adapter.quote(tmp_column) }} {{ new_column_type }};
    update {{ relation }} set {{ adapter.quote(tmp_column) }} = {{ adapter.quote(column_name) }};
    alter table {{ relation }} drop column {{ adapter.quote(column_name) }} cascade;
    alter table {{ relation }} rename column {{ adapter.quote(tmp_column) }} to {{ adapter.quote(column_name) }}
  {% endcall %}

{% endmacro %}



{% macro alter_relation_add_remove_columns(relation, add_columns = none, remove_columns = none) -%}
  {{ return(adapter.dispatch('alter_relation_add_remove_columns', 'dbt')(relation, add_columns, remove_columns)) }}
{% endmacro %}

{% macro vertica__alter_relation_add_remove_columns(relation, add_columns, remove_columns) %}
  
  {% if add_columns is none %}
    {% set add_columns = [] %}
  {% endif %}
  {% if remove_columns is none %}
    {% set remove_columns = [] %}
  {% endif %}
  
  {% set sql -%}
     
     alter {{ relation.type }} {{ relation }}
       
            {% for column in add_columns %}
               add column {{ column.name }} {{ column.data_type }}{{ ',' if not loop.last }}
            {% endfor %}{{ ',' if remove_columns | length > 0 }}
            
            {% for column in remove_columns %}
                drop column {{ column.name }}{{ ',' if not loop.last }}
            {% endfor %}
  
  {%- endset -%}

  {% do run_query(sql) %}

{% endmacro %}


{# 
  No need to implement get_columns_in_query(). Syntax supported by default. 
#}