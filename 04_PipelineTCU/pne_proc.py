import pandas as pd
import os

if __name__ == '__main__':
    diretorio = "./constants/Dados_saida_eletricidade"
    cont = 0
    lista = [a[2] for a in os.walk(diretorio)]
    for arquivo in lista[0]:
        for sheet_name, df in pd.read_excel(diretorio + '/' + arquivo, sheet_name=None).items():
            if sheet_name == "ResumoDécadas_comGD" :
                df.drop('Unnamed: 0', axis=1, inplace=True)
                colunas_mantidas = df.columns[:5]
                df = df[colunas_mantidas]
                df_pot_acumulada = df.iloc[32:44]
                df_pot_incremental= df.iloc[76:88]
                df_geracao_pot_medio = df.iloc[120 : 132]
                df_atendimento_a_ponta = df.iloc[154 : 166]
                df_emissoes_totais = df.iloc[169 : 172]
                break