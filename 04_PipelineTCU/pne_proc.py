import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    diretorio = "./constants/Dados_saida_eletricidade"
    ctes = "./constants/"
    cont = 0
    lista = [a[2] for a in os.walk(diretorio)]
    cenarios = ctes + "Cenarios_PNE/"
    cols1 = ["Fonte/Tecnologia", "Ano 2015","Ano 2030","Ano 2040","Ano 2050"]
    cols2 = ["Fonte/Tecnologia", "Intervalo 2015","Intervalo 2015-2030","Intervalo 2031-2040","Intervalo 2041-2050"]
    cols3 = ["Período", "Ano 2015","Ano 2030","Ano 2040","Ano 2050"]
    cols4 = ["Tipo Expansão", "Ano 2015"]
    for arquivo in lista[0]:
        for sheet_name, df in pd.read_excel(diretorio + '/' + arquivo, sheet_name=None).items():
            if sheet_name == "ResumoDécadas_comGD" :
                arquivo = arquivo.split(".xlsm")[0]
                loc = cenarios + arquivo + ".xlsx"
                writer = pd.ExcelWriter(loc, engine="openpyxl")
                df.drop('Unnamed: 0', axis=1, inplace=True)
                colunas_mantidas = df.columns[:5]
                df = df[colunas_mantidas]
                df_pot_acumulada = df.iloc[32:43]        
                linhas_ant = range(32,43)
                df_pot_acumulada.iloc[:, 1:] = df_pot_acumulada.iloc[:, 1:].applymap(lambda x : int(x))
                df_pot_acumulada.to_excel(writer,sheet_name="Potencia Acumulada - SIN (MW)", header=cols1, index=False)
                df_geracao_per_medio = df.iloc[120 : 131]
                df_geracao_per_medio.iloc[:, 1:] = df_geracao_per_medio.iloc[:, 1:].applymap(lambda x : int(x))
                df_geracao_per_medio.to_excel(writer,sheet_name="Geracao Periodo Medio (MWMed)", header=cols1, index=False)
                df_atendimento_a_ponta = df.iloc[154 : 165]
                df_atendimento_a_ponta.iloc[:, 1:] = df_atendimento_a_ponta.iloc[:, 1:].applymap(lambda x : int(x))
                df_atendimento_a_ponta.to_excel(writer,sheet_name="Atendimento a Ponta(MW)",header=cols1, index=False)
                df_pot_incremental= df.iloc[76:87]
                df_pot_incremental.iloc[:, 1:] = df_pot_incremental.iloc[:, 1:].applymap(lambda x : int(x))
                df_pot_incremental.to_excel(writer,sheet_name="Potencia Incremental - SIN(MW)", header=cols2, index=False)
                df_emissoes_totais = df.iloc[169 : 171]
                df_emissoes_totais.iloc[:, 1:] = df_emissoes_totais.iloc[:, 1:].applymap(lambda x : int(x))
                df_emissoes_totais.to_excel(writer,sheet_name="Emissoes Totais (MtCO2eq)",  header=cols3, index=False)
                df_custo_total = df[184:186]
                df_custo_total.drop(df.columns[2:], axis=1, inplace=True)
                df_custo_total.iloc[:, 1:] = df_custo_total.iloc[:, 1:].applymap(lambda x : int(x))
                df_custo_total.iloc[0, 0] = "Expansão Centralizada"
                df_custo_total.iloc[1, 0] = "Expansão por GD"
                df_custo_total.to_excel(writer,sheet_name="Custo Total (bilhões de R$)", index=False, header=cols4)
                writer.close()
                break 