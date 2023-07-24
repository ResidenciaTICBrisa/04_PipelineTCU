import streamlit as st
from components.add_logo import add_logo

def menu_lateral():
    add_logo()
    st.header("Dashboard")
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)