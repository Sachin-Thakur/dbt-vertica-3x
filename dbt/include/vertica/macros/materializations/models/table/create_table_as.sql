{% macro vertica__create_table_as(temporary, relation, sql) -%}
  {%- set sql_header = config.get('sql_header', none) -%}


  {{ sql_header if sql_header is not none }}
  {%- set order_by = config.get('order_by', none) -%}
 
 {%- set segmented_by_string = config.get('segmented_by_string', default=none) -%}
  {%- set segmented_by_all_nodes = config.get('segmented_by_all_nodes', default=true) -%}
  {%- set no_segmentation = config.get('no_segmentation', default=False) -%}
  {%- set ksafe = config.get('ksafe', default=None) -%}


  {%- set partition_by_string = config.get('partition_by_string', default=none) -%}
  {%- set partition_by_group_by_string = config.get('partition_by_group_by_string', default=none) -%}


  {%- set partition_by_active_count = config.get('partition_by_active_count', default=none) -%}
  



  create {% if temporary: -%}local temporary{%- endif %} table
    {{ relation.include(database=(not temporary), schema=(not temporary)) }}
    {% if temporary: -%}on commit preserve rows{%- endif %}
  as (
    {{ sql }}
  )

 {% if order_by is not none  %}
 order by {{ order_by  }}

{%- endif -%}


  {% if segmented_by_string is not none -%}

       segmented by {{ segmented_by_string }} {% if segmented_by_all_nodes %} ALL NODES

   {% endif %}
  {% endif %}

  {% if no_segmentation %} UNSEGMENTED ALL NODES {% endif %}

 {% if ksafe is not none -%}
  ksafe {{ ksafe }}
  {% endif %}
  



{% if partition_by_string is not none -%}
    ; alter table {{ relation.include(database=(not temporary), schema=(not temporary)) }} partition BY {{ partition_by_string }}
    {% if partition_by_string is not none and partition_by_group_by_string is not none -%}
      group by {{ partition_by_group_by_string }}
    {% endif %}
    {% if partition_by_string is not none and partition_by_active_count is not none %}
      SET ACTIVEPARTITIONCOUNT {{ partition_by_active_count }}
    {% endif %}
  {% endif %}  
  ;


    



  
{% endmacro %}

{% macro vertica__create_table_from_relation(temporary, relation, target, dest_columns, sql) -%}
  {%- set sql_header = config.get('sql_header', none) -%}
  {%- set table_schema = vertica__get_table_in_relation(target) -%}
  {%- set dest_cols_csv = get_quoted_csv(dest_columns | map(attribute="name")) -%}

  {{ sql_header if sql_header is not none }}

  create {% if temporary: -%}local temporary{%- endif %} table {{ relation }}
      (
      {% for row in table_schema %}
        {{ row.column_name }} {{ row.data_type }}
        {%- if not loop.last %}, {% endif %}
      {% endfor %}
      ) on commit preserve rows;

      insert into {{ relation }} ({{ dest_cols_csv }})
      (
        select {{ dest_cols_csv }} from (
         {{ sql }}
        ) as DBT_MASKED_TARGET
      );

{% endmacro %}