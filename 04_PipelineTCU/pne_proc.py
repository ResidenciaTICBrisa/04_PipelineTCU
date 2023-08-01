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
    for arquivo in lista[0]:
        for sheet_name, df in pd.read_excel(diretorio + '/' + arquivo, sheet_name=None).items():
            if sheet_name == "ResumoDécadas_comGD" :
                arquivo = arquivo.split(".xlsm")[0]
                loc = cenarios + arquivo + ".xlsx"
                writer = pd.ExcelWriter(loc, engine="openpyxl")
                df.drop('Unnamed: 0', axis=1, inplace=True)
                df.drop('Unnamed: 1', axis=1, inplace=True)
                colunas_mantidas = df.columns[:4]
                df = df[colunas_mantidas]
                df_pot_acumulada = df.iloc[32:43]                
                linhas = [
                    "Hidro",
                    "Gas Natural",
                    "Carvao",
                    "Nuclear",
                    "Oleos Comb",
                    "Biomassa",
                    "Eolica",
                    "Solar",
                    "Outros",
                    "Pot Compl",
                    "GD"
                ]
                linhas_ant = range(32,43)
                cols = ["2015","2030","2040","2050"]
                cols_ant = df_pot_acumulada.columns[0:4].values.tolist()
                ren_col = {cols_ant[j]: cols[j] for j in range(len(cols_ant))}
                ren_lin = {linhas_ant[i]: linhas[i] for i in range(len(linhas_ant))}
                df_pot_acumulada.rename(columns=ren_col, index = ren_lin, inplace=True)
                df_pot_acumulada = df_pot_acumulada.applymap(lambda x : int(x))
                df_pot_acumulada.to_excel(writer,sheet_name="Potencia Acumulada - SIN (MW)")
                df_geracao_per_medio = df.iloc[120 : 131]
                linhas_ant = range(120,131)
                ren_lin = {linhas_ant[i]: linhas[i] for i in range(len(linhas_ant))}
                df_geracao_per_medio.rename(columns=ren_col, index = ren_lin, inplace=True)
                df_geracao_per_medio = df_geracao_per_medio.applymap(lambda x : int(x))
                df_geracao_per_medio.to_excel(writer,sheet_name="Geracao Periodo Medio (MWMed)")
                df_atendimento_a_ponta = df.iloc[154 : 165]
                linhas_ant = range(154,165)
                ren_lin = {linhas_ant[i]: linhas[i] for i in range(len(linhas_ant))}
                df_atendimento_a_ponta.rename(columns=ren_col, index = ren_lin, inplace=True)
                df_atendimento_a_ponta = df_atendimento_a_ponta.applymap(lambda x : int(x))
                df_atendimento_a_ponta.to_excel(writer,sheet_name="Atendimento a Ponta(MW)")
                df_pot_incremental= df.iloc[76:87]
                cols = ["2015","2015-2030","2031-2040","2041-2050"]
                ren_col = {cols_ant[j]: cols[j] for j in range(len(cols_ant))}
                linhas_ant = range(76,87)
                ren_lin = {linhas_ant[i]: linhas[i] for i in range(len(linhas_ant))}
                df_pot_incremental.rename(columns=ren_col, index = ren_lin, inplace=True)
                df_pot_incremental = df_pot_incremental.applymap(lambda x : int(x))
                df_pot_incremental.to_excel(writer,sheet_name="Potencia Incremental - SIN(MW)")
                cols = ["2015","2030","2040","2050"]
                linhas = ["P Medio", "P Critico", "Teto"]
                linhas_ant = range(169, 172)
                df_emissoes_totais = df.iloc[169 : 172]
                ren_col = {cols_ant[j]: cols[j] for j in range(len(cols_ant))}
                ren_lin = {linhas_ant[i]: linhas[i] for i in range(len(linhas_ant))}
                df_emissoes_totais.rename(index=ren_lin, columns=ren_col, inplace=True)
                df_emissoes_totais = df_emissoes_totais.applymap(lambda x : int(x))
                df_emissoes_totais.to_excel(writer,sheet_name="Emissoes Totais (MtCO2eq)")
                df_custo_total = df[184:186]
                df_custo_total.drop(df.columns[0], axis=1, inplace=True)
                df_custo_total.drop(df.columns[2:], axis=1, inplace=True)
                linhas_ant = range(184,186)
                linhas = ["Expansao Centralizada", "Expansao por GD", "Total"]
                ren_lin = {linhas_ant[i] : linhas[i] for i in range(len(linhas_ant))}
                ren_col = {"Unnamed: 3" : "Custo"}
                df_custo_total.rename(index=ren_lin, columns=ren_col, inplace=True)
                df_custo_total = df_custo_total.applymap(lambda x : int(x))
                df_custo_total.to_excel(writer,sheet_name="Custo Total (bilhões de R$)")
                writer.close()
                break