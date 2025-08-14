import streamlit as st

# Inject custom CSS to make the main container full width

#st.markdown(
APP_CSS= """
    <style>
        .stMainBlockContainer {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
            max-width: 100% !important;
        }
        .memo-container {
            background-color: white;
            padding: 20px;
            margin-top: 28px;
            color: black;
            border: 1px solid #ddd;
            border-radius: 8px;
            line-height: 1.5em;
            height: 400px;
        }

        .memo-title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .memo-section-title {
            font-size: 20px;
            font-weight: bold;
            margin-top: 15px;
        }

        .memo-paragraph {
            font-size: 16px;
            margin: 8px 0;
        }

        .memo-table table {
            border-collapse: collapse;
            width: 100%;
            margin: 8px 0;
        }

        .memo-table td, .memo-table th {
            border: 1px solid black;
            padding: 4px;
            text-align: left;
        }

        .highlight {
            background-color: yellow;
        }

    </style>
    """
#    unsafe_allow_html=True
#)