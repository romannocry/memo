import streamlit as st
import openpyxl
import json
import pandas as pd
import os
from word_engine import *
from load_tab import render_load_tab
from preview import render_preview_tab

# Inject custom CSS to make the main container full width
st.markdown(
    """
    <style>
        .stMainBlockContainer {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
            max-width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar override uploads
st.sidebar.header("📁 Override Inputsss")
uploaded_excel = st.sidebar.file_uploader("Upload Excel File", type=["xlsx"])
uploaded_json = st.sidebar.file_uploader("Upload Mapping File (JSON)", type=["json"])

DEFAULT_CONFIG_PATH = "config.json"
DEFAULT_VARIABLES_PATH = "variables.json"
# --- Load Mapping ---
if uploaded_json:
    config_file = uploaded_json
    st.success("✅ Using uploaded JSON mapping")
else:
    config_file = DEFAULT_CONFIG_PATH
    #st.info("ℹ️ Using default mapping file")

# Read JSON mapping
if isinstance(config_file, str):
    with open(config_file, "r") as f:
        raw_json = f.read()
else:
    raw_json = config_file.read().decode("utf-8")

# Read JSON variables
if isinstance(DEFAULT_VARIABLES_PATH, str):
    with open(DEFAULT_VARIABLES_PATH, "r") as f:
        variables_json = f.read()
else:
    variables_json = config_file.read().decode("utf-8")
    
variables_file = json.loads(variables_json)

# Parse JSON mapping into a Python dictionary
config_file = json.loads(raw_json)
placeholders = config_file.get("placeholders", {})
memo_structure = config_file.get("memo_structure", {})

# --- Load Excel ---
if uploaded_excel:
    excel_file = uploaded_excel
    st.success("✅ Using uploaded Excel file")
else:
    excel_file = config_file.get("settings", {}).get("excel_file")
    #st.info("ℹ️ Using default Excel file")


# Read Excel file
wb = openpyxl.load_workbook(excel_file, data_only=True)


tabs = {
    "Load": lambda: render_load_tab(variables_file, wb),
    #"Config Editor": lambda: render_load_tab(variables_file, wb),
    "Preview": lambda: render_preview_tab(memo_structure, placeholders)
}

# Create tab objects
tab_objs = st.tabs(tabs.keys())

# Render each tab's content
for tab_obj, render_func in zip(tab_objs, tabs.values()):
    with tab_obj:
        render_func()