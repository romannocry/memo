import streamlit as st

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