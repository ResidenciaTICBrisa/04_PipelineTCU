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


def roundColumn(df, col):
    """
    Arredonda as precisões dos elementos de uma coluna para duas casas decimais

    Args:
        df (DataFrame): Data Frame que armazena a coluna cujos elementos se deseja arredondar
        col (int): índice da coluna cujos elementos se deseja arredondar

    Retorna: DataFrame
    """
    i = 0
    while i < len(df):
        div = str(df.iloc[i, col]).split('.')
        esq = div[0]
        dir = div[1][0:3:]
        while len(dir) < 3:
            dir += '0'
        div = esq + dir
        num = int(div)
        if num % 10 > 4:
            num += 10
        num -= num % 10
        df.iloc[i, col] = num / 1000
        i += 1
    return df


class AnuarioANPHandler:
    """
    Uma classe que lê os arquivos csv Anuário Estatístico da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis, trata eles e cria arquivos com os dados desses arquivos tratados.

    Atributos:
        path_inicio (str): caminho até a pasta onde os arquivos originais estão salvos.
        path_final (str): caminho até a pasta ondes os arquivos derivados das tabelas originais serão salvos.s

    Métodos:
        def generateTablesGN(self, dic_tab_nomes):
            Gera as tabela com os dados das tabelas procuradas do Anuário Estatístico da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis relacionadas ao Panorama Internacional de Reservas, Produção e Consumo de Gás Natural
        def generateTablesPetGNNac(self, dic_tab_nomes):
            Gera as tabela com os dados das tabelas procuradas do Anuário Estatístico da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis relacionadas a Indústria Nacional de Petróleo e Gás Natural
        def generateTablesBioCombs(self, dic_tab_nomes):
            Gera as tabela com os dados das tabelas procuradas do Anuário Estatístico da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis relacionadas a Biocombustíveis
        def generateTablesCBIO(self, dic_tab_nomes, year):
            Gera as tabela com os dados das tabelas procuradas do Anuário Estatístico da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis relacionadas a Emissão e Aposentadoria de CBIOs
    """

    def __init__(self, path_inicio, path_final):
        """
        Construtor da classe AnuarioANPHandler.

        Args:
            path_inicio (str): caminho até a pasta onde os arquivos originais estão salvos.
            path_final (str): caminho até a pasta ondes os arquivos derivados das tabelas originais serão salvos.
        """

        self.path_inicio = path_inicio
        self.path_final = path_final
        os.makedirs(self.path_final, exist_ok=True)

    def generateTablesGN(self, dic_tab_nomes):
        """
        Gera as tabela com os dados das tabelas procuradas do Anuário Estatístico da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis relacionadas ao Panorama Internacional de Reservas, Produção e Consumo de Gás Natural

        Args:
            dic_tab_nomes (dict[str,list]): Dicionário cujo nome do arquivo original é a chave e contém as informações da tabela tratada que são o índice da coluna que deve ser apagada e o nome da 2ª coluna da tabela tratada

        Retorna: bool: Verdadeiro se todas as tabelas foram encontradas, Falso caso contrário.
        """

        try:
            n_tabelas = 0
            for key in dic_tab_nomes.keys():
                df = pd.read_csv(self.path_inicio + key, encoding="utf-16", delimiter=';', decimal=',')
                lim = dic_tab_nomes[key][1]
                df.drop(df.columns[0:lim], axis=1, inplace=True)
                df = drop_row_by_text(df, "Outros")
                df = drop_row_by_text(df, "Total")
                df = roundColumn(df, 1)
                maiores = []
                pais = df.iloc[0, 0]
                comp = 1
                while df.iloc[comp, 0] == pais:
                    comp += 1
                i = comp - 1
                while i < len(df):
                    maiores.append([df.iloc[i, 1], df.iloc[i, 0]])
                    i += comp
                maiores.sort(reverse=True)
                maiores = maiores[0:10]
                nomes_maiores = []
                for maior in maiores:
                    nomes_maiores.append(maior[1])
                nomes_maiores.append("Brasil")
                i = 0
                while i < len(df):
                    if df.iloc[i, 0] in nomes_maiores:
                        i += comp
                    else:
                        df.drop(index=df.iloc[i: i + comp].index, inplace=True)
                df.to_csv(self.path_final + dic_tab_nomes[key][0], index=False, header=["pais", dic_tab_nomes[key][2], "ano"])
                n_tabelas += 1
            return n_tabelas == len(dic_tab_nomes)
        except Exception:
            return False

    def generateTablesPetGNNac(self, dic_tab_nomes):
        """
        Gera as tabela com os dados das tabelas procuradas do Anuário Estatístico da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis relacionadas a Indústria Nacional de Petróleo e Gás Natural

        Args:
            dic_tab_nomes (dict[str,list]): Dicionário cujo nome do arquivo original é a chave e que contém as informações relacionadas ao nome da tabela tratada e o nome da 2ª coluna da tabela tratada

        Retorna: bool: Verdadeiro se todas as tabelas foram encontradas, Falso caso contrário.
        """

        n_tabelas = 0
        try:
            for key in dic_tab_nomes.keys():
                df = pd.read_csv(self.path_inicio + key, encoding="utf-16", delimiter=';', decimal=',')
                df.drop(df.columns[0:1], axis=1, inplace=True)
                df = roundColumn(df, 2)
                df.to_csv(self.path_final + dic_tab_nomes[key][0], index=False, header=["localizacao", "ano", dic_tab_nomes[key][1]])
                n_tabelas += 1
            return n_tabelas == len(dic_tab_nomes)
        except Exception:
            return False

    def generateTablesBioCombs(self, dic_tab_nomes):
        """
        Gera as tabela com os dados das tabelas procuradas do Anuário Estatístico da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis relacionadas a Biocombustíveis

        Args:
            dic_tab_nomes (dict[str,list]): Dicionário cujo nome do arquivo original é a chave e que contém as informações relacionadas ao nome da tabela tratada e o nome da 2ª coluna da tabela tratada

        Retorna: bool: Verdadeiro se todas as tabelas foram encontradas, Falso caso contrário.
        """

        n_tabelas = 0
        try:
            for key in dic_tab_nomes.keys():
                df = pd.read_csv(self.path_inicio + key, encoding="utf-16", delimiter=';', decimal=',')
                df.drop(df.columns[1:2], axis=1, inplace=True)
                df = roundColumn(df, 1)
                df.to_csv(self.path_final + dic_tab_nomes[key][0], index=False, header=["regiao", dic_tab_nomes[key][1], "ano"])
                n_tabelas += 1
            return n_tabelas == len(dic_tab_nomes)
        except Exception:
            return False

    def generateTablesCBIO(self, dic_tab_nomes, year):
        """
        Gera as tabela com os dados das tabelas procuradas do Anuário Estatístico da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis relacionadas a Emissão e Aposentadoria de CBIOs

        Args:
            dic_tab_nomes (dict[str,list]): Dicionário cujo nome do arquivo original é a chave e que contém as informações relacionadas ao nome da tabela tratada e os nomes da 2ª e da 3ª colunas da tabela tratada
            year (int): ano do qual os dados das tabelas pertencem

        Retorna: bool: Verdadeiro se todas as tabelas foram encontradas, Falso caso contrário.
        """

        n_tabelas = 0
        try:
            for key in dic_tab_nomes.keys():
                df = pd.read_csv(self.path_inicio + key, encoding="utf-16", delimiter=';', decimal=',')
                df["ano"] = [year] * len(df)
                df.to_csv(self.path_final + dic_tab_nomes[key][0], index=False, header=["mes", dic_tab_nomes[key][1], dic_tab_nomes[key][2], "ano"])
                n_tabelas += 1
            return n_tabelas == len(dic_tab_nomes)
        except Exception:
            return False
