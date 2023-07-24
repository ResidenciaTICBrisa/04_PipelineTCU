import streamlit as st
import pandas as pd
import numpy as np
from pages import home, dashboard, sobre
from st_on_hover_tabs import on_hover_tabs
  
st.sidebar.markdown("# Page 2 ❄️")  
def show():
    st.title("Home")
    st.write("Bem-vindo à página inicial!")
    st.image("assets/tcu-logo.png", caption="Minha Imagem", use_column_width=True)
show()