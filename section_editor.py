import streamlit as st
from typing import List, Dict
import json

def section_editor(structure: dict) -> dict:
    st.markdown("## 📝 Memo Section Editor", unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .section-block {
            border: 1px solid #ccc;
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 0.5rem;
            background-color: #f9f9f9;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Load existing structure
    sections = structure.get("sections", [])
    updated_sections = []

    # Title input
    title = st.text_input("📄 Document Title", value=structure.get("title", ""))

    st.markdown("---")

    # Section Editor
    for i, section in enumerate(sections):
        with st.container():
            st.markdown('<div class="section-block">', unsafe_allow_html=True)

            section_title = st.text_input(f"Section Title {i+1}", value=section["title"], key=f"title_{i}")
            content = st.text_area(f"Content", value=section["content"], key=f"content_{i}", height=150)

            # Delete section
            if st.button("❌ Remove this section", key=f"remove_{i}"):
                continue  # skip this section

            updated_sections.append({
                "title": section_title,
                "content": content
            })

            st.markdown('</div>', unsafe_allow_html=True)

    # Add new blank section
    if st.button("➕ Add New Section"):
        updated_sections.append({
            "title": "New Section",
            "content": ""
        })

    # Final structure
    updated_structure = {
        "title": title,
        "sections": updated_sections
    }

    # Preview
    st.markdown("### 📦 Preview JSON Output")
    st.json(updated_structure)

    return updated_structure
