import streamlit as st

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://logodownload.org/wp-content/uploads/2017/11/tcu-logo-tribunal-de-contas-da-uniao.png);
                background-repeat: no-repeat;
                background-size: 150px 140px; /* Ajuste o tamanho da imagem aqui */
                padding-top: 120px;
                background-position: 50px 30px;
            }
            [data-testid="stSidebarNav"]::before {
                
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )