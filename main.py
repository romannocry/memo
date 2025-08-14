import streamlit as st
import openpyxl
import json
import os
import sys
import importlib

# ---  MODULES  ---
from pages import load_tab, preview
from shared import utils, css
from shared.css import APP_CSS


# --- RELOAD DEV MODULES ---
DEV_MODULE_PREFIXES = ["pages.", "shared."]
for module_name in list(sys.modules.keys()):
    if any(module_name.startswith(prefix) for prefix in DEV_MODULE_PREFIXES):
        importlib.reload(sys.modules[module_name])

# --- CONTINUE WITH STREAMLIT APP ---
st.markdown(APP_CSS, unsafe_allow_html=True)
st.sidebar.header("📁 Override Inputs")

wb = openpyxl.load_workbook("./inputs/input_data.xlsx", data_only=True)

tabs = {
    "Load parameters": lambda: load_tab.render_load_tab(utils.read_json_file('./config/variables.json'), wb),
    "Render Preview": lambda: preview.render_preview_tab(wb),  # No parameters needed for now
    # other tabs...
}


tab_objs = st.tabs(tabs.keys())
for tab_obj, render_func in zip(tab_objs, tabs.values()):
    with tab_obj:
        render_func()
