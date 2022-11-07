{%- macro current_timestamp() -%}
    {{ adapter.dispatch('current_timestamp', 'dbt')() }}
{%- endmacro -%}

{% macro vertica__current_timestamp() -%}
  {{ exceptions.raise_not_implemented(
    'current_timestamp macro not implemented for adapter ' + adapter.type()) }}
{%- endmacro %}

{%- macro snapshot_get_time() -%}
    {{ adapter.dispatch('snapshot_get_time', 'dbt')() }}
{%- endmacro -%}

{% macro vertica__snapshot_get_time() %}
    {{ current_timestamp() }}
{% endmacro %}