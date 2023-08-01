import streamlit as st
from components.menu_lateral import menu_lateral
from components.add_logo import add_logo

def show():
    # Renderizando o menu lateral apenas uma vez
    menu_lateral()
    add_logo()
    
    st.title("DATABASE")
    st.write("Bem-vindo à página inicial!")
    
    
    st.title("Bases de dados utilizadas")
    options = st.multiselect(
    'Escolha um cenário',
    ['Novo cenário', 'Políticas P&D',],
    ['Novo cenário', 'Políticas P&D'])

    st.write('You selected:', options)
    
    st.title("Pipeline TCU")
    st.text('Pipeline de dados e análises para modelagem de curvas de custo de marginal de abatimento do carbono das diversas alternativas do setor energético brasileiro para fins de suportar avaliação de custo-efetividade de políticas de transição energética do país.')
show()