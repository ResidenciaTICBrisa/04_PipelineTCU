import math
import pandas as pd

class BenHandler:
    # Uma classe que lê o arquivo correspondente às matrizes energéticas consolidadas do Balanço Energético Nacional (BEN), seleciona e transforma as tabelas desejadas, além de salvar o resultado em uma única tabela em arquivo csv com os dados da matrizes consolidades do Balanço Energético Nacional de 1970 até o ano mais atual.

    # Atributos:
    #   file (str): nome do arquivo que será lido
    #   path (str): caminho até a pasta onde os arquivos serão salvos

    # Métodos:
    #   def drop_row_by_text(self, df, text):
    #       Exclui uma linha de um Data Frame com base no texto da sua primeira célula
    #   def generateTable(self):   
    #       Gera a tabela com os dados das matrizes consolidadas do BEN de 1970 até o ano mais atual


    def __init__(self, file, path_final):
        # Construtor da classe BenHandler.
        # Args:
        #     file (str): nome do arquivo correspondente às matrizes energéticas consolidadas do Balanço Energético Nacional (BEN),
        #     path_final (str): caminho até a pasta ondes os arquivos serão salvos.
        self.file = file
        self.path = path_final

    def drop_row_by_text(self, df, text):
        # Exclui uma linha de um Data Frame com base no texto da sua primeira célula
        # Args:
        #     df (DataFrame): Data Frame que armazena a linha que se deseja apagar
        #     text (str): texto que a linha a ser excluída contém
        index_to_drop = df[df.iloc[:, 0].str.contains(text)].index
        df.drop(index=index_to_drop, inplace=True)
        return df

    def generateTable(self):   
        # Gera a tabela com os dados das matrizes consolidadas do BEN de 1970 até o ano mais atual
        cont = False
        df_total = pd.DataFrame()
        titulos = ['CONTA',
                   'PRODUÇÃO',
                   'IMPORTAÇÃO',
                   'VARIAÇÃO DE ESTOQUES',
                   'EXPORTAÇÃO',
                   'NÃO-APROVEITADA',
                   'REINJEÇÃO',
                   'CONSUMO FINAL NÃO-ENERGÉTICO',
                   'SETOR ENERGÉTICO',
                   'RESIDENCIAL',
                   'COMERCIAL',
                   'PÚBLICO',
                   'AGROPECUÁRIO',
                   'RODOVIÁRIO',
                   'FERROVIÁRIO',
                   'AÉREO',
                   'HIDROVIÁRIO',
                   'INDUSTRIAL - TOTAL']
        for sheet_name, df in pd.read_excel(self.path + self.file, sheet_name=None).items():
            df.drop('Unnamed: 0', axis=1, inplace=True)
            df.dropna(inplace=True)
            i = 0
            while len(df.index) != 18:
                titulo = df.iloc[i,0]
                while titulo[0] == ' ':
                    titulo = titulo[1:]
                while titulo[-1] == ' ':
                    titulo = titulo[0:-1]             
                if titulo in titulos:
                    df.iloc[i,0] = titulo
                    i += 1
                else:
                    df.drop(index=df.iloc[i].name, inplace=True)
            df = df.transpose()
            num_rows = len(df)
            new_column_data = [sheet_name] * num_rows
            df['Ano'] = new_column_data
            df.iloc[0, -1] = 'Ano'
            if cont:
                df.drop(index=df.iloc[0].name, inplace=True)
            cont = True
            df = self.drop_row_by_text(df, 'ENERGIA SECUNDÁRIA TOTAL ')
            df = self.drop_row_by_text(df,'ENERGIA PRIMÁRIA TOTAL')
            df = self.drop_row_by_text(df,'TOTAL')
            df_total = pd.concat([df_total,df])
        signal = lambda y : 1 if (y >= 0) else -1
        df_total.iloc[1:,1:-1] = df_total.iloc[1:,1:-1].applymap(lambda x : math.floor(abs(x))*signal(x) if (abs(x)*10 - int(abs(x))*10) < 5 else math.ceil(abs(x))*signal(x))
        df_total.iloc[1:,1:-1]=df_total.iloc[1:,1:-1].astype('int64') 
        df_total.to_csv(self.path + "BEN_total.csv", index=False, header=False) 