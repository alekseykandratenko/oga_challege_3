import streamlit as st
from .load_config import load_theme

def load_css():
    theme = load_theme()
    
    with open("styles/principal.css") as f:
        st.markdown(
            f"""
                <style>
                    :root {{
                        --primarylColor: {theme["primaryColor"]};
                        --backgroundColor: {theme["backgroundColor"]};
                        --secondaryBackgroundColor: {theme["secondaryBackgroundColor"]};
                    }}
                    {f.read()}
                </style>
            """
            , unsafe_allow_html=True
        )