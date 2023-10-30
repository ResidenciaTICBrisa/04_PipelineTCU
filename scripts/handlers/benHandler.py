import math
import os
import pandas as pd


def drop_row_by_text(df, text):
    """
    Exclui uma linha de um Data Frame com base no texto da sua primeira célula

    Args:
        df (DataFrame): Data Frame que armazena a linha que se deseja apagar
        text (str): texto que a linha a ser excluída contém

    Retorna: DataFrame
    """

    index_to_drop = df[df.iloc[:, 0].str.contains(text)].index
    df.drop(index=index_to_drop, inplace=True)
    return df


def field_signal(y):
    """
    Retorna o sinal de y

    Args:
        y (int): número cujo sinal será analisado

    Retorna: 1 se o número for maior ou igual a zero ou -1 caso ele seja menor que a zero.
    """
    if y < 0:
        return -1
    return 1


class BenHandler:
    """
    Uma classe que lê o arquivo das matrizes energéticas consolidadas do Balanço Energético Nacional de 1970 até o ano mais atual disponível, seleciona e transforma as tabelas desejadas e salva o resultado em uma única tabela em csv.

    Atributos:
        file (str): nome do arquivo que será lido
        path_inicio (str): caminho até a pasta onde o arquivo original está salvo.
        path_final (str): caminho até a pasta onde o arquivo derivado da tabela do arquivo original será salvo.

    Métodos:
        def generateTable(self):
            Gera a tabela com os dados das matrizes consolidadas do BEN de 1970 até o ano mais atual
    """

    def __init__(self, file, path_inicio, path_final):
        """
        Construtor da classe BenHandler.

        Args:
            file (str): nome do arquivo correspondente às matrizes energéticas consolidadas do Balanço Energético Nacional (BEN),
            path_inicio (str): caminho até a pasta onde o arquivo original está salvo.
            path_final (str): caminho até a pasta onde o arquivo derivado da tabela do arquivo original será salvo.
        """

        self.file = file
        self.path_inicio = path_inicio
        self.path_final = path_final
        os.makedirs(self.path_final, exist_ok=True)

    def generateTable(self):
        """
        Gera a tabela com os dados das matrizes consolidadas do BEN de 1970 até o ano mais atual

        Retorna: bool: Verdadeiro se foi possível gerar uma tabela reunindo todas as informações desejadas, Falso caso contrário.
        """

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
        try:
            for sheet_name, df in pd.read_excel(self.path_inicio + self.file, sheet_name=None).items():
                df.drop('Unnamed: 0', axis=1, inplace=True)
                df.dropna(inplace=True)
                i = 0
                while len(df.index) != 18:
                    titulo = df.iloc[i, 0]
                    while titulo[0] == ' ':
                        titulo = titulo[1:]
                    while titulo[-1] == ' ':
                        titulo = titulo[0:-1]
                    if titulo in titulos:
                        df.iloc[i, 0] = titulo
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
                df = drop_row_by_text(df, 'ENERGIA SECUNDÁRIA TOTAL ')
                df = drop_row_by_text(df, 'ENERGIA PRIMÁRIA TOTAL')
                df = drop_row_by_text(df, 'TOTAL')
                df_total = pd.concat([df_total, df])
            df_total.iloc[1:, 1:-1] = df_total.iloc[1:, 1:-1].applymap(lambda x : math.floor(abs(x)) * field_signal(x) if (abs(x) * 10 - int(abs(x)) * 10) < 5 else math.ceil(abs(x)) * field_signal(x))
            df_total.iloc[1:, 1:-1] = df_total.iloc[1:, 1:-1].astype('int64')
            if len(df_total):
                df_total.to_csv(self.path_final + "BEN_total.csv", index=False, header=False)
            return len(df_total)
        except Exception:
            return False
