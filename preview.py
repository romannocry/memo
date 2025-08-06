

import streamlit as st
import openpyxl
import json
import pandas as pd
import re

def resolve_placeholders(text, placeholder_values):
    # Replace {{key}} with corresponding value from placeholder_values
    def replacer(match):
        key = match.group(1)
        return str(placeholder_values.get(key, f"{{{{{key}}}}}"))  # leave untouched if not found

    return re.sub(r"\{\{(\w+)\}\}", replacer, text)

def render_preview_tab(memo_structure: dict, placeholder_values: dict):

    
    # Display summary as a table
    st.title("Memo Preview")
    st.text(placeholder_values)
    #st.text(resolve_placeholders(memo_structure,placeholder_values))