import math
import pandas as pd

class ComunicacaoHandler:
    # Uma classe que lê o arquivo correspondente às emissões de Gases de Efeito Estufa (GEE) consolidadas da Comunicação Nacional do Brasil à Convenção-Quadro das Nações Unidas sobre Mudanças do Clima, transforma a tabela desejada, além de salvar o resultado em uma única tabela em arquivo csv com os dados das emissões de Gases de Efeito Estufa (GEE) consolidadas.

    # Atributos:
    #     path (str): caminho até o arquivo de origem,
    #     path_final (str): caminho até a pasta ondes os arquivos serão salvos.

    # Métodos:
    #   def drop_row_by_text(self, df, text):
    #       Exclui uma linha de um Data Frame com base no texto da sua primeira célula
    #   def transfColInt(self, df):
    #       Transforma todas as colunas do tipo float64 de um tabela para o tipo int 64 e retorna a tabela transformada
    #   def generateTable(self):   
    #       Gera a tabela com os dados das emissões de Gases de Efeito Estufa (GEE) consolidadas.

    def __init__(self, file, path_raiz, path_final):
        # Construtor da classe BenHandler.
        # Args:
        #     file (str): nome do arquivo de origem. 
        #     path_raiz (str): caminho até o arquivo de origem.
        #     path_final (str): caminho até a pasta ondes os arquivos serão salvos.
        self.path = path_raiz + file
        self.path_final = path_final

    def transfColInt(self, df):
        # Transforma todas as colunas do tipo float64 de um tabela para o tipo int 64 e retorna a tabela transformada
        #Args:
        #    df (DataFrame): DataFrame da tabela que será manipulada
        # Retorna: DataFrame
        for c in df.columns:
            if df[c].dtype ==  'float64':
                df[c] = df[c].astype('int64') 
        return df

    def drop_row_by_text(self, df, text):
        # Exclui uma linha de um Data Frame com base no texto da sua primeira célula
        # Args:
        #     df (DataFrame): Data Frame que armazena a linha que se deseja apagar
        #     text (str): texto que a linha a ser excluída contém
        # Retorna: DataFrame
        index_to_drop = df[df.iloc[:, 0].str.contains(text)].index
        df.drop(index=index_to_drop, inplace=True)
        return df

    def generateTable(self):   
        # Gera a tabela com os dados das emissões de Gases de Efeito Estufa (GEE) consolidadas.
        dict_file = pd.read_excel(self.path, sheet_name=None)
        for k in dict_file.keys():
            df = dict_file[k]
            i = 0
            while str(df.iloc[i,0]).find("GWP-1 (SAR)") == -1:
                df.drop(index=df.iloc[i].name, inplace=True)
            df_ano = df.iloc[1:2,:]
            df_ano.dropna(axis=1, inplace=True)
            for c in df_ano.columns:
                if df_ano[c].dtype ==  'float64':
                   df_ano[c] = df_ano[c].astype('int64')
            df.dropna(inplace=True)
            df = self.drop_row_by_text(df, 'TOTAL')
            df.drop(index=df.iloc[-1].name, inplace=True)
            df_tot = pd.DataFrame()
            df_aux = df.iloc[:,0:1]
            i = 0
            tam = df_ano.columns.size
            num_rows = len(df_aux)
            df = df.iloc[:,1:]
            df.iloc[:,:] = df.iloc[:,:].applymap(lambda x : math.floor(x) if (x*10 - int(x)*10) < 5 else math.ceil(x))
            df = self.transfColInt(df)
            while i < tam:
                new_column_data = [df_ano.iloc[0, i]] * num_rows
                df_aux['Ano'] = new_column_data
                df_aux['Emissoes'] = df.iloc[:,0:1]
                df = df.iloc[:,1:] 
                df_tot = pd.concat([df_tot, df_aux])
                i += 1
            cols = ["Setor", "Ano", "Emissoes"]
            df_tot.to_csv(self.path_final + 'Comunicao.csv', header=cols, index=False) 