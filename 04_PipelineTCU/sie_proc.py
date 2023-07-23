import pandas as pd
import numpy as np
from pathlib import Path

if __name__ == '__main__' : 
    arquivo = "reporte_dinamico_emisiones.xlsx" 
    path = str(Path(__file__).parent.resolve()) 
    path += "/constants/" 
    for sheet_name, df in pd.read_excel(path + arquivo, sheet_name=None).items():
        if(sheet_name == 'E'):
            cont = 0
            df.drop('Unnamed: 0', axis=1, inplace=True)
            df.drop('Unnamed: 2', axis=1, inplace=True)
            df = df.where((pd.notnull(df)), None)
            indice = 0
            for ano in range(2018, 2022):
                indice = (ano - 2018)*5
                while True:
                    if df.iloc[indice,0] is None:
                        df.drop(cont, axis=0, inplace=True)
                        cont += 1
                    elif df.iloc[indice,0].find(str(ano)) == -1:
                        df.drop(cont, axis=0, inplace=True)
                        cont += 1
                    else: 
                        for cont_aux in range(0,3):
                            df.drop(cont, axis=0, inplace=True)
                            cont += 1
                        break
                ind_set = 0
                while ind_set < 5:
                    cont += 1
                    ind_set += 1
            indice += 5
            df.drop(df.index[indice:], inplace=True)
            df.drop('Unnamed: 1', axis=1, inplace=True)
            dfs_anos = []
            df.fillna(0, inplace=True)
            arr = df.to_numpy()
            totais = []
            for ano in range(2018, 2022):
                setores = ['G','T','I','O','T']
                fontes = ['P','G','C','T']
                indice = (ano - 2018)*5
                df_aux = pd.DataFrame(arr[indice:indice+5], setores, fontes)
                totais.append(arr[indice+4][3])
                dfs_anos.append(df_aux)
                df_aux.to_csv(path + str(ano) + ".csv")
            df_totais = pd.DataFrame(np.array(totais), range(2018, 2022), ['T'])
            df_totais.to_csv(path + "Emissoes_Totais_SIE.csv")
            