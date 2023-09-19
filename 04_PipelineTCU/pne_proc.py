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
    cols1 = ["Fonte/Tecnologia", "Ano 2015","Ano 2030","Ano 2040","Ano 2050", "Cenário"]
    cols2 = ["Período", "Ano 2015","Ano 2030","Ano 2040","Ano 2050", "Cenário"]
    cols3 = ["Tipo Expansão", "Ano 2012", "Ano 2015", "Cenário"]
    df_pot_acum = pd.DataFrame()
    df_ger_per_med = pd.DataFrame()
    df_atend_ponta = pd.DataFrame()
    df_em_totais = pd.DataFrame()
    df_custo_total = pd.DataFrame()
    df_cons_gas_nat = pd.DataFrame()
    for arquivo in lista[0]:
        for sheet_name, df in pd.read_excel(diretorio + '/' + arquivo, sheet_name=None, header=None).items():
            if sheet_name == "ResumoDécadas_comGD" :
                arquivo = arquivo.split(".xlsm")[0]
                df.drop(df.columns[0:1], axis=1, inplace=True)
                colunas_mantidas = df.columns[:5]
                df = df[colunas_mantidas]
                df_aux = df.iloc[33:44]
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].astype(int)
                num_rows = len(df_aux)
                new_column_data = [arquivo] * num_rows
                df_aux['Cenário'] = new_column_data
                df_pot_acum = pd.concat([df_pot_acum, df_aux])
                df_aux = df.iloc[121 : 132]
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : int(x))
                num_rows = len(df_aux)
                new_column_data = [arquivo] * num_rows
                df_aux['Cenário'] = new_column_data
                df_ger_per_med = pd.concat([df_ger_per_med, df_aux])
                df_aux = df.iloc[155 : 166]
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : int(x))
                num_rows = len(df_aux)
                new_column_data = [arquivo] * num_rows
                df_aux['Cenário'] = new_column_data
                df_atend_ponta = pd.concat([df_atend_ponta, df_aux])
                df_aux = df.iloc[170 : 172]
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : int(x))
                num_rows = len(df_aux)
                new_column_data = [arquivo] * num_rows
                df_aux['Cenário'] = new_column_data
                df_em_totais = pd.concat([df_em_totais, df_aux])
                df_aux = df.iloc[176:178]
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : int(x))
                num_rows = len(df_aux)
                new_column_data = [arquivo] * num_rows
                df_aux['Cenário'] = new_column_data
                df_cons_gas_nat = pd.concat([df_cons_gas_nat, df_aux])
                df_aux = df.iloc[185:187]
                df_aux.drop(df.columns[3:], axis=1, inplace=True)
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : int(x))
                num_rows = len(df_aux)
                df_aux.iloc[0, 0] = "Expansão Centralizada"
                df_aux.iloc[1, 0] = "Expansão por GD"
                new_column_data = [arquivo] * num_rows
                df_aux['Cenário'] = new_column_data
                df_custo_total = pd.concat([df_custo_total, df_aux])
                num_rows = len(df_aux)
                new_column_data = [arquivo] * num_rows
                df_aux['Cenário'] = new_column_data
                break
    if not os.path.exists(cenarios):
        os.makedirs(cenarios)
    df_pot_acum.to_csv(cenarios + 'PotAcumPNE.csv', header=cols1, index=False)
    df_ger_per_med.to_csv(cenarios + 'GerPerMedPNE.csv', header=cols1, index=False)
    df_atend_ponta.to_csv(cenarios + 'AtendPontaPNE.csv', header=cols1, index=False)
    df_em_totais.to_csv(cenarios + 'EmTotPNE.csv', header=cols2, index=False)
    df_custo_total.to_csv(cenarios + 'CustoTotPNE.csv', header=cols3, index=False)
    df_cons_gas_nat.to_csv(cenarios + 'ConsGasNatPNE.csv', header=cols2, index=False)
