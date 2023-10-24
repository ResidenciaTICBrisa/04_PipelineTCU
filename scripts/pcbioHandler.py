from datetime import datetime
import math
import pandas as pd
import re

class PCBIOHandler:
    # Uma classe que lê o arquivo correspondente à Memória de Cálculo do Preço Médio de Descarbonização e as metas de descarbonização das distribuidoras, transforma as tabela desejadas, além de salvar os resultados em arquivos csv com os dados do volume negociado dos créditos de descarbonização e as metas de descarbonização das distribuidoras.

    # Atributos:
    #     path (str): caminho onde até o arquivo de origem
    #     path_final (str): caminho até a pasta ondes os arquivos serão salvos

    # Métodos:
    #   def generateTable(self):   
    #       Gera as tabela com os dados correspondentes à Memória de Cálculo do Preço Médio de Descarbonização e as metas de descarbonização das distribuidoras

    def __init__(self, file, path_raiz, path_final):
        # Construtor da classe PCBIOHandler.
        # Args:
        #     file (str): nome do arquivo de origem.
        #     path_raiz (str): caminho onde até o arquivo de origem.
        #     path_final (str): caminho até a pasta ondes os arquivos serão salvos.
        #     file_final (str): nome do arquivo final.
        self.path = path_raiz + file
        self.path_final = path_final

    def generateTable(self):
        # Gera as tabelas com os dados correspondentes à Memória de Cálculo do Preço Médio de Descarbonização e as metas de descarbonização das distribuidoras
        n_tabelas = 0
        for sheet_name, df in pd.read_excel(self.path, sheet_name=None).items(): 
            if(sheet_name == "VCBIO"):
                df.drop('Unnamed: 0', axis=1, inplace=True)
                while str(df.iloc[0,0]) != 'data':
                    df.drop(index=df.iloc[0].name, inplace=True)
                i = 1
                while i < len(df):
                    try: 
                        df.iloc[i,0] = datetime.strptime(str(df.iloc[i,0]), '%Y-%m-%d %H:%M:%S').date()
                        i += 1
                    except Exception:
                        df.drop(index=df.iloc[i].name, inplace=True)
                df.dropna(axis=1, inplace=True)
                i = 1
                while i < len(df.columns):
                    if df.iloc[0,i] != 'valor financeiro' and df.iloc[0,i] != 'qtde negociada':
                        df.drop(df.columns[i], axis=1, inplace=True)
                    else:
                        i += 1
                df.iloc[1:,2:] = df.iloc[1:,2:].applymap(lambda x : math.floor(x) if (x*10 - int(x)*10) < 5 else math.ceil(x))
                num_rows = len(df)
                new_column_data = ['0'] * num_rows
                df['mes'] = new_column_data
                df['ano'] = new_column_data
                i = 1
                while i < len(df):
                    df.iloc[i,3] = df.iloc[i,0].month
                    df.iloc[i,4] = df.iloc[i,0].year
                    i += 1
                df.iloc[0,1] = "qtde_negociada"
                df.iloc[0,2] = "valor_financeiro"
                df.iloc[0,3] = "mes"
                df.iloc[0,4] = "ano"
                df.to_csv(self.path_final + sheet_name + '.csv', index=False, header=False) 
                n_tabelas += 1
            elif(sheet_name == "meta CBIO"):
                df.drop('Unnamed: 0', axis=1, inplace=True)
                df.dropna(inplace=True)
                df.drop(df.iloc[:,-1].name, axis=1, inplace=True)
                ano_atual = 0
                ano_atual = re.search("[0-5][0-9][0-9][0-9]", df.iloc[0,2]).group()
                df.iloc[0,2] = "meta_CNPE"
                df.iloc[0,3] = "meta_nao_cumprida"
                new_column_data = len(df) * [ano_atual]
                df['ano'] = new_column_data
                df.iloc[0,-1] = "ano"
                df.iloc[0,0] = "razao_social"
                i = 1
                df.iloc[1:,2:] = df.iloc[1:,2:].applymap(lambda x : '0' if (x == '') else x)  
                df.to_csv(self.path_final + sheet_name + '.csv', index=False, header=False)     
                n_tabelas += 1
            if n_tabelas == 2:
                break
            