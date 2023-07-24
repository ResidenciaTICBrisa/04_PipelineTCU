import streamlit as st
import pandas as pd
import numpy as np
from pages import dashboard
from components.menu_lateral import menu_lateral
from components.add_logo import add_logo


def main():
    menu_lateral()
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
  
    st.markdown("# Página princial 🎈")
        # Mostrando a página selecionada
        
if __name__ == "__main__":
    main()




