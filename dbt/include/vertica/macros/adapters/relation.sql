{% macro make_temp_relation(base_relation, suffix='__dbt_tmp') %}
  {{ return(adapter.dispatch('make_temp_relation', 'dbt')(base_relation, suffix)) }}
{% endmacro %}

{% macro vertica__make_temp_relation(base_relation, suffix) %}
    {% set tmp_identifier = base_relation.identifier ~ suffix %}
    {% do return(base_relation.incorporate(
                                  path={
                                    "identifier": tmp_identifier,
                                    "schema": none,
                                    "database": none
                                  })) -%}
{% endmacro %}


{% macro rename_relation(from_relation, to_relation) -%}
  {{ return(adapter.dispatch('rename_relation', 'dbt')(from_relation, to_relation)) }}
{% endmacro %}

{% macro vertica__rename_relation(from_relation, to_relation) %}
  {% set target_name = adapter.quote_as_configured(to_relation.identifier, 'identifier') %}
  {% call statement('rename_relation') -%}
    alter {{ from_relation.type }} {{ from_relation }} rename to {{ target_name }}
  {%- endcall %}
{% endmacro %}

-- a user-friendly interface into adapter.get_relation
{% macro load_cached_relation(relation) %}  
  {% do return(adapter.get_relation(
    database=relation.database,
    schema=relation.schema,
    identifier=relation.identifier
  )) -%}
{% endmacro %}
-- old name for backwards compatibility
{% macro load_relation(relation) %}
    {{ return(load_cached_relation(relation)) }}
{% endmacro %}

-- load relation call 
{% macro vertica__load_relation(relation) -%}
  {{ return(load_relation(relation)) }}
{%- endmacro %}


{#
  No need to implement drop_relation(). Syntax supported by default. 
  No need to implement drop_relation_if_exists(). Syntax supported by default.
  No need to implement get_or_create_relation(). Syntax supported by default.
#}

{% macro make_intermediate_relation(base_relation, suffix='__dbt_tmp') %}
  {{ return(adapter.dispatch('make_intermediate_relation', 'dbt')(base_relation, suffix)) }}
{% endmacro %}

{% macro vertica__make_intermediate_relation(base_relation, suffix) %}
    {{ return(vertica__make_temp_relation(base_relation, suffix)) }}
{% endmacro %}




{% macro make_backup_relation(base_relation, backup_relation_type, suffix='__dbt_backup') %}
    {{ return(adapter.dispatch('make_backup_relation', 'dbt')(base_relation, backup_relation_type, suffix)) }}
{% endmacro %}

{% macro vertica__make_backup_relation(base_relation, backup_relation_type, suffix) %}
    {%- set backup_identifier = base_relation.identifier ~ suffix -%}
    {%- set backup_relation = base_relation.incorporate(
                                  path={"identifier": backup_identifier},
                                  type=backup_relation_type
    ) -%}
    {{ return(backup_relation) }}
{% endmacro %}



{% macro truncate_relation(relation) -%}
  {{ return(adapter.dispatch('truncate_relation', 'dbt')(relation)) }}
{% endmacro %}

{% macro vertica__truncate_relation(relation) -%}
  {% call statement('truncate_relation') -%}
    truncate table {{ relation }}
  {%- endcall %}
{% endmacro %}
