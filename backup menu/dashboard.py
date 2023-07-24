import streamlit as st
import pandas as pd
import numpy as np
from pages import home, dashboard, sobre
from components.menu_lateral import menu_lateral
from st_on_hover_tabs import on_hover_tabs



def show():
    
    
    st.title("Dashboard")
    st.write("Bem-vindo à página inicial!")
    st.image("assets/tcu-logo.png", caption="Minha Imagem", use_column_width=True)
    
     #df = pd.read_csv("https://raw.githubusercontent.com/ResidenciaTICBrisa/04_PipelineTCU/dashboard_app/data/energia.csv")
    
    st.title('Dashboard')
    st.write('Bem vindo ao dashboard')

    tab1, tab2 = st.tabs(["📈 Gráfico", "🗃 Dados"])
    
   #Caixa de seleção
    #option = st.selectbox(
    #    'Seletor de gráfico',
     #   ('Emissões CO2e', 'Emissões por poluente', 'Financeiro: Custo/economia'))

    #st.write('Você selecionou:', option)
   
   #Gráfico
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["Produto 1", "Produto 2", "Produto 3"])
    
   #Data slider
    #start_time = st.slider(
    #    "Qual é a data inicial",
    #    value=(2020))
    
    #st.write("Start time:", start_time)

    tab1.subheader("Efeitos por Política: Curva de Custo do Abatimento de CO2e")
   # tab1.selectbox(option)
    tab1.bar_chart(chart_data)
   # tab1.slider(start_time)
    

    tab2.subheader("Tabela de dados")
    tab2.write(chart_data)