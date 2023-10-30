import math
import os
import pandas as pd


def formatacaoComum(df, apaga_ultimo, e_inteiro, apaga_prim):
    """
    Formata e retorna as tabelas com uma formatação comum a todas

    Args:
        df (DataFrame): DataFrame da tabela que será formatada
        apaga_ultimo (bool): variável que informa se é necessário apagar a última linha da tabela
        e_inteiro (bool): variável que informa se é necessário converter as colunas para int64
        apaga_prim (bool): variável que informa se é necessário apagar a linha de índice 1

    Retorna: DataFrame
    """

    df.dropna(inplace=True)
    coluna = 1
    n_cols = df.columns.size
    while coluna < n_cols:
        if isinstance(df.iloc[0, coluna], str):
            df.drop(df.columns[coluna:], axis=1, inplace=True)
            break
        coluna += 1
    if apaga_ultimo:
        df.drop(index=df.iloc[-1].name, inplace=True)
    if apaga_prim:
        df.drop(index=df.iloc[1].name, inplace=True)
    if e_inteiro:
        df.iloc[:, 1:] = df.iloc[:, 1:].applymap(lambda x : math.floor(x) if (x * 10 - int(x) * 10) < 5 else math.ceil(x))
        for c in df.columns:
            if df[c].dtype == 'float64':
                df[c] = df[c].astype('int64')
    return df


def tabelasConsRegioes(df, regioes, apaga_primeiros):
    """
    Formata e retorna as tabelas que mostram os tipos de Consumo nas regiões geográficas do Brasil

    Args:
        df (DataFrame): DataFrame da tabela que será formatada
        regioes (list[str]): lista com os nomes das regiões
        apaga_primeiros (bool): variável se informa se é necessário apagar as primeiras linhas da tabela

    Retorna: DataFrame
    """

    if apaga_primeiros:
        df.drop(df.iloc[1:7].index, inplace=True)
    linha = 1
    while linha < len(regioes) + 1:
        if not df.iloc[linha, 0] in regioes:
            df.drop(index=df.iloc[linha].name, inplace=True)
        else:
            linha += 1
    df.drop(index=df.iloc[7:].index, inplace=True)
    return df


class AnuarioHandler:
    """
    Uma classe que lê o arquivo correspondente ao Anuário Estatístico de Energia Elétrica, seleciona e transforma as tabelas desejadas e salva as tabelas resultantes em arquivos csv.

    Atributos:
      file (str): nome do arquivo que será lido
      n_tabelas (str): número de tabelas que o arquivo conseguiu criar, inicialmente é zero
      path_inicio (str): caminho até a pasta onde o arquivo original está salvo.
      path_final (str): caminho até a pasta ondes os arquivos derivados das tabelas do arquivo original serão salvos.

    Métodos:
        def formataSalvaTabela(self, df, nome_tab, cols):
            Formata uma tabela para adicionar o ano do dado como uma coluna e salva essa tabela como arquivo csv
        def generateTables(self):
            Formata e salva todas as tabelas do Anuário Estatístico de Energia Elétrica em arquivos csv
    """

    def __init__(self, file, path_inicio, path_final):
        """
        Construtor da classe AnuarioHandler.

        Args:
            file (str): nome do arquivo correspondente ao  arquivo do Anuário Estatístico de Eletricidade.
            path_inicio (str): caminho até a pasta onde o arquivo original está salvo.
            path_final (str): caminho até a pasta ondes os arquivos derivados das tabelas do arquivo original serão salvos.
        """
        self.file = file
        self.n_tabelas = 0
        self.path_inicio = path_inicio
        self.path_final = path_final
        os.makedirs(self.path_inicio, exist_ok=True)
        os.makedirs(self.path_final, exist_ok=True)

    def formataSalvaTabela(self, df, nome_tab, cols):
        """
        Formata uma tabela para adicionar o ano do dado como uma coluna e salva essa tabela como arquivo csv

        Args:
           df (DataFrame): DataFrame da tabela que será transformado e salvo como csv
           nome_tab (str): Nome do arquivo csv no qual o DataFrame será salvo
           cols (list[str]): Lista com os nomes das colunas que será o header do arquivo csv
        """

        df_final = pd.DataFrame()
        ind_col = 1
        while ind_col < len(df.columns):
            df_aux = df.iloc[1:, 0:1]
            num_rows = len(df_aux)
            new_column_data = [df.iloc[0, ind_col]] * num_rows
            df_aux['Ano'] = new_column_data
            df_aux['Geracao'] = df.iloc[1:, ind_col]
            df_final = pd.concat([df_final, df_aux])
            ind_col += 1
        df_final['Ano'] = df_final['Ano'].astype('int64')
        df_final.to_csv(self.path_final + nome_tab, header=cols, index=False)

    def generateTables(self):
        """
        Formata e salva todas as tabelas do Anuário Estatístico de Energia Elétrica em arquivos csv

        Retorna: bool: Verdadeiro se todas as tabelas foram encontradas, Falso caso contrário.
        """

        cols1 = ["Pais", "Ano", "Cap_Inst"]
        cols2 = ["Pais", "Ano", "Geracao"]
        dictCapInst = {
            "Capacidade instalada de geração renovável no mundo" :
            "CapInstRenPaises(GW).csv",
            "Capacidade instalada de geração nuclear no mundo" :
            "CapInstNucPaises(GW).csv",
            "Capacidade instalada de geração térmica fóssil no mundo" :
            "CapInstTermFosPaises(GW).csv",
            "Capacidade instalada de geração hidrelétrica no mundo":
            "CapInstHidPaises(GW).csv",
            "Capacidade instalada de geração eólica no mundo":
            "CapInstEolPaises(GW).csv",
            "Capacidade instalada de geração solar no mundo":
            "CapInstSolPaises(GW).csv",
            "Capacidade instalada de geração biomassa no mundo":
            "CapInstBioPaises(GW).csv"
        }
        dictGer = {
            "Geração renovável no mundo": "GerRenPaises(TWh).csv",
            "Geração nuclear no mundo": "GerNucPaises(TWh).csv",
            "Geração térmica fóssil no mundo" : "GerTermFosPaises(TWh).csv",
            "Geração hidrelétrica no mundo": "GerHidPaises(TWh).csv",
            "Geração eólica no mundo": "GerEolPaises(TWh).csv",
            "Geração solar no mundo": "GerSolPaises(TWh).csv",
            "Geração biomassa no mundo": "GerBioPaises(TWh).csv"
        }
        dictCapGerEm = {
            "Capacidade instalada de geração elétrica no Brasil (MW)": [False, True, True, "CapInstFonte(MW).csv", ["Fonte", "Ano", "Cap_Inst"]],
            "Geração elétrica por fonte no Brasil (GWh)": [False, True, True, "GelElFonte(GWh).csv", ["Fonte", "Ano", "Geracao"]],
            "Emissões de GEE no SIN - MtCO2": [False, False, True, "EmGEESIN(MtCO2).csv", ["Fonte", "Ano", "Emissoes"]],
            "Emissões de GEE no Sistema Isolado - MtCO2": [False, False, True, "EmGEESistIso(MtCO2).csv", ["Fonte", "Ano", "Emissoes"]],
            "Emissões de GEE provenientes da Geração Elétrica no Brasil - MtCO2": [False, False, True, "EmGEEGerEl(MtCO2).csv", ["Subsistema", "Ano", "Emissoes"]]
        }
        keysCapInst = dictCapInst.keys()
        keysGer = dictGer.keys()
        keysCapGerEm = dictCapGerEm.keys()
        for sheet_name, df in pd.read_excel(self.path_inicio + self.file, sheet_name=None).items():
            try:
                if self.n_tabelas == 24:
                    break
                df.drop('Unnamed: 0', axis=1, inplace=True)
                passou = False
                for key in keysCapInst:
                    if df.iloc[5, 0].find(key) != -1:
                        df = formatacaoComum(df, True, True, True)
                        self.formataSalvaTabela(df, dictCapInst[key], cols1)
                        self.n_tabelas += 1
                        passou = True
                        break
                if passou:
                    continue
                passou = False
                for key in keysGer:
                    if df.iloc[5, 0].find(key) != -1:
                        df = formatacaoComum(df, True, True, True)
                        self.formataSalvaTabela(df, dictGer[key], cols2)
                        self.n_tabelas += 1
                        passou = True
                        break
                if passou:
                    continue
                passou = False
                for key in keysCapGerEm:
                    if df.iloc[5, 0].find(key) != -1:
                        df = formatacaoComum(df, dictCapGerEm[key][0], dictCapGerEm[key][1], dictCapGerEm[key][2])
                        self.formataSalvaTabela(df, dictCapGerEm[key][3], dictCapGerEm[key][4])
                        self.n_tabelas += 1
                        passou = True
                        break
                if passou:
                    continue
                if df.iloc[5, 0].find("Consumo médio total por subsistema, região e UF") != -1:
                    regioes = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste", "Regiões geográficas"]
                    cols3 = ["Subsistema", "Ano", "Cons_Med_Tot"]
                    df = formatacaoComum(df, False, False, True)
                    self.formataSalvaTabela(df.iloc[0:7, :], 'ConsMedTotSubsis(kWh_mes).csv', cols3)
                    df = tabelasConsRegioes(df, regioes, True)
                    cols3 = ["Regiao", "Ano", "Cons_Med_Tot"]
                    self.formataSalvaTabela(df, 'ConsMedTotReg(kWh_mes).csv', cols3)
                    self.n_tabelas += 2
                elif df.iloc[5, 0].find("Consumo médio residencial por subsistema, região e UF") != -1:
                    regioes = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste", "Regiões geográficas"]
                    cols3 = ["Subsistema", "Ano", "Cons_Med_Res"]
                    df = formatacaoComum(df, False, False, True)
                    self.formataSalvaTabela(df.iloc[0:7, :], 'ConsMedResSubsis(kWh_mes).csv', cols3)
                    df = tabelasConsRegioes(df, regioes, True)
                    cols3 = ["Regiao", "Ano", "Cons_Med_Res"]
                    self.formataSalvaTabela(df, 'ConsMedResReg(kWh_mes).csv', cols3)
                    self.n_tabelas += 2
                elif df.iloc[5, 0].find("Consumo médio anual per capita por região e UF (kWh/hab)") != -1:
                    regioes = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste", "Brasil"]
                    cols3 = ["Regiao", "Ano", "Cons_Med_An_PC"]
                    df = formatacaoComum(df, False, False, False)
                    df = tabelasConsRegioes(df, regioes, False)
                    self.formataSalvaTabela(df, 'ConsMedAnPerCapReg(kWh_hab).csv', cols3)
                    self.n_tabelas += 1
            except Exception:
                continue
        return self.n_tabelas == 24
