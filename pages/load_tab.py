import streamlit as st
import openpyxl
import json
import pandas as pd

__all__ = ['get_cell_value','render_load_tab']  # Only 'greet' will be importable via 'from mymodule import *'

def get_cell_value(wb, typ, sheet, cells = ""):
    try:
        if typ == "cell":
            return wb[sheet][cells].value
        elif typ == "range":
            ws = wb[sheet]
            cells = ws[cells]
            return [[c.value for c in row] for row in cells]
        elif typ == "chart":
            return f"Chart at {cells}"  # Placeholder
    except Exception as e:
        return f"❌ {e.__class__.__name__}: {str(e)}"
    return "N/A"

def render_load_tab(variables: dict, wb: openpyxl.Workbook):

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(variables, orient="index")
    df.index.name = "Name"
    df.reset_index(inplace=True)

    # Add resolved value
    df["resolved_value"] = df.apply(lambda row: get_cell_value(wb, row["type"], row["sheet"], row["cells"]), axis=1)

    # Display editor
    edited_df = st.data_editor(
        df,
        column_config={
            "Name": st.column_config.TextColumn("Name"),
            "type": st.column_config.SelectboxColumn("Type", options=["cell", "range", "chart"]),
            "sheet": st.column_config.TextColumn("Sheet name"),
            "cells": st.column_config.TextColumn("Cells (e.g., A1 or A1:B2)"),
            "value": st.column_config.TextColumn("Reference (e.g., Sheet1!A1)"),
            "resolved_value": st.column_config.TextColumn("📎 Excel Value"),
        },
        disabled=["resolved_value"],  # Make it read-only
        num_rows="dynamic",
        use_container_width=True
    )

    # Rebuild placeholder dict
    updated_variables = {
        row["Name"]: {"type": row["type"], "sheet": row["sheet"], "cells": row["cells"]}
        for _, row in edited_df.iterrows()
        if row["Name"] and row["type"] and row["sheet"] and row["cells"]
    }

    if st.button("💾 Save Changes"):
        with open("variables.json", "w") as f:
            json.dump(updated_variables, f, indent=4)
        st.success("✅ Config saved to `variables.json`")
        st.rerun()

    return ""#updated_variables