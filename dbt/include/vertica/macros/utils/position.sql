{% macro vertica__position(substring_text, string_text) %}

    strpos(
        {{ string_text }},
        {{ substring_text }}

    )

{%- endmacro -%}