

import streamlit as st
import openpyxl
import json
import pandas as pd
import re
from pages.load_tab import *

__all__ = ['render_preview_tab','resolve_placeholders']

def resolve_placeholders(text, placeholder_values, wb):
    # Replace {{key}} with corresponding value from placeholder_values
    def replacer(match):
        key = match.group(1)
        if key in placeholder_values:
            value = placeholder_values[key]
            return get_cell_value(wb, value.get("type"), value.get("sheet"), value.get("cells"))
        else:
            return str(value)
        #return str(placeholder_values.get(key, f"{{{{{key}}}}}"))  # leave untouched if not found

    return re.sub(r"\{\{(\w+)\}\}", replacer, text)

def render_preview_tab(memo_structure: dict, placeholder_values: dict, wb: openpyxl.Workbook):

    DEFAULT_STRUCTURE_PATH = "structure.json"

    # Load JSON structure from file
    try:
        with open(DEFAULT_STRUCTURE_PATH, "r", encoding="utf-8") as f:
            structure_json = json.load(f)
    except Exception as e:
        st.error(f"Failed to load structure file: {e}")
        return

    # Display the JSON as text or parsed object
    st.title("Memo Preview")
    st.text(resolve_placeholders(str(structure_json), placeholder_values, wb))  # Renders nicely formatted and expandable JSON
    #st.text(resolve_placeholders(memo_structure,placeholder_values))