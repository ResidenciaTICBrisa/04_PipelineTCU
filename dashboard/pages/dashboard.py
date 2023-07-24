import streamlit as st
from components.menu_lateral import menu_lateral
import pandas as pd
import numpy as np
from datetime import datetime
from PIL import Image


def show():
    # Renderizando o menu lateral apenas uma vez
    menu_lateral()
    
    #df = pd.read_csv("https://raw.githubusercontent.com/ResidenciaTICBrisa/04_PipelineTCU/dashboard_app/data/energia.csv")
    
    st.write('Bem vindo ao dashboard')
    col1, col2 = st.columns([3, 1])
    data = np.random.randn(10, 1)
    
    col1.subheader("Gráfico")
    col1.line_chart(data)

    
    col2.chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["Produto 1", "Produto 2", "Produto 3"])
    
    # Seleção de containers
    tab1, tab2 = st.tabs(["📈 Gráfico", "🗃 Dados"])
    
    ano = st.slider('Selecione o ano', 2016, 2050, 2023)
    
    # Slider ano
    st.write("O ", ano, 'selecionado')
    
   #Caixa de seleção
    #option = st.selectbox(
    #    'Seletor de gráfico',
    #   ('Emissões CO2e', 'Emissões por poluente', 'Financeiro: Custo/economia'))

    #st.write('Você selecionou:', option)
   
   #Gráfico 1
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
    
    
    st.title("Bases de dados utilizadas")
    options = st.multiselect(
    'Escolha um cenário',
    ['Novo cenário', 'Políticas P&D',],
    ['Novo cenário', 'Políticas P&D'])

    st.write('You selected:', options)
    
    st.title("Pipeline TCU")
    st.text('Pipeline de dados e análises para modelagem de curvas de custo de marginal de abatimento do carbono das diversas alternativas do setor energético brasileiro para fins de suportar avaliação de custo-efetividade de políticas de transição energética do país.')
show()