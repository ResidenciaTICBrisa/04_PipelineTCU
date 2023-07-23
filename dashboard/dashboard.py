import streamlit as st
import pandas as pd
import numpy as np
from st_on_hover_tabs import on_hover_tabs
from datetime import datetime
from PIL import Image

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.sidebar:
        tabs = on_hover_tabs(tabName=['Dashboard', 'Database', 'Sobre o projeto'], 
                             iconName=['dashboard', 'money', 'economy'],
                             styles = {'navtab': {'background-color':'#111',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key="1")

if tabs =='Dashboard':
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
    


    

elif tabs == 'Database':
    st.title("Bases de dados utilizadas")
    options = st.multiselect(
    'Escolha um cenário',
    ['Novo cenário', 'Políticas P&D',],
    ['Novo cenário', 'Políticas P&D'])

    st.write('You selected:', options)



elif tabs == 'Sobre o projeto':
    st.title("Pipeline TCU")
    st.text('Pipeline de dados e análises para modelagem de curvas de custo de marginal de abatimento do carbono das diversas alternativas do setor energético brasileiro para fins de suportar avaliação de custo-efetividade de políticas de transição energética do país.')




             