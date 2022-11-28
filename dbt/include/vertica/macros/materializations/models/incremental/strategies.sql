{% macro get_insert_into_sql(target_relation, temp_relation, unique_key, dest_columns) %}

    {%- set dest_cols_csv = get_quoted_csv(dest_columns | map(attribute="name")) -%}

    
    
    {% if unique_key %}
        delete from {{ target }}
            where (
                {{ unique_key }}) in (
                select ({{ unique_key }})
                from {{ source }}
            );

    {% endif %}

    insert into {{ target_relation }} ({{ dest_cols_csv }})
    (
        select {{ dest_cols_csv }}
        from {{ temp_relation }}
    )
   

   
{% endmacro %}

{% macro get_incremental_append_sql(target_relation, temp_relation, dest_columns, unique_key) %}

  {{ return(adapter.dispatch('get_incremental_append_sql', 'dbt')(target_relation, temp_relation, dest_columns, unique_key)) }}

{% endmacro %}


{% macro vertica__get_incremental_append_sql(target_relation, tmp_relation, unique_key,dest_columns) %}

  {% do return(get_insert_into_sql(target_relation, tmp_relation, unique_key, dest_columns)) %}

{% endmacro %}
{% macro get_incremental_delete_insert_sql(arg_dict) %}

  {{ return(adapter.dispatch('get_incremental_delete_insert_sql', 'dbt')(arg_dict)) }}

{% endmacro %}


{% macro vertica__get_incremental_delete_insert_sql(arg_dict) %}

  {% do return(get_delete_insert_merge_sql(arg_dict["target_relation"], arg_dict["temp_relation"], arg_dict["unique_key"], arg_dict["dest_columns"])) %}

{% endmacro %}

{% macro get_incremental_merge_sql(arg_dict) %}

  {{ return(adapter.dispatch('get_incremental_merge_sql', 'dbt')(arg_dict)) }}

{% endmacro %}

{% macro vertica__get_incremental_merge_sql(arg_dict) %}

  {% do return(get_merge_sql(arg_dict["target_relation"], arg_dict["temp_relation"], arg_dict["unique_key"], arg_dict["dest_columns"])) %}

{% endmacro %}





{% macro get_incremental_insert_overwrite_sql(arg_dict) %}

  {{ return(adapter.dispatch('get_incremental_insert_overwrite_sql', 'dbt')(arg_dict)) }}

{% endmacro %}


{% macro vertica__get_incremental_insert_overwrite_sql(arg_dict) %}

  {% do return(get_insert_overwrite_merge_sql(arg_dict["target_relation"], arg_dict["temp_relation"], arg_dict["dest_columns"], arg_dict["predicates"])) %}

{% endmacro %}






{% macro get_incremental_default_sql(arg_dict) %}

  {{ return(adapter.dispatch('get_incremental_default_sql', 'dbt')(arg_dict)) }}

{% endmacro %}




{% macro vertica__get_incremental_default_sql(target_relation, tmp_relation, unique_key, dest_columns) %}

  {% do return(get_incremental_append_sql(target_relation, tmp_relation, unique_key,dest_columns)) %}

{% endmacro %}