import math
import os
import warnings
import pandas as pd
warnings.filterwarnings("ignore")


def transfColInt(df):
    """
    Transforma todas as colunas do tipo float64 de um tabela para o tipo int 64 e retorna a tabela transformada
    Args:
        df (DataFrame): DataFrame da tabela que será manipulada

    Retorna: DataFrame
    """

    for c in df.columns:
        if df[c].dtype == 'float64':
            df[c] = df[c].astype('int64')
    return df


def formatTable(df, limInf, limSup, arquivo):
    """
    Transforma uma tabela num determinado intervalo em um data frame e retorna o data frame da tabela escolhida e tratada

    Args:
        df (DataFrame): DataFrame da tabela que será manipulada
        limInf (int): limite inferior em que se encontram as linhas escolhidas
        limSup (int): limite superior em que se encontram as linhas escolhidas
        arquivo (str): nome do arquivo/simulação ao qual a tabela pertence

    Retorna: DataFrame
    """

    df = df.iloc[limInf:limSup]
    df.iloc[:, 1:] = df.iloc[:, 1:].applymap(lambda x: math.floor(x) if (x * 10 - int(x) * 10) < 5 else math.ceil(x))
    num_rows = len(df)
    new_column_data = [arquivo] * num_rows
    df['Cenário'] = new_column_data
    return df


class PNEHandler:
    """
    Uma classe que lê os arquivo correspondentes às simulações do PNE 2050, seleciona e transforma as tabelas desejadas, além de salvar as tabelas resultantes em arquivos csv com os dados das simulações desejados.

    Atributos:
        path_inicio (str): caminho até a pasta onde o arquivo original está salvo.
        path_final (str): caminho até a pasta ondes os arquivos derivados das tabelas do arquivo original serão salvos.

    Métodos:
        def saveTable(self, df, fileName, cols):
          Salva uma tabela na pasta de destino
        def generaterTables(self):
          Gera as tabelas do PNE 2050
    """

    def __init__(self, path_inicio, path_final):
        """
        Construtor da classe PNEHandler.

        Args:
            path_inicio (str): caminho até a pasta onde o arquivo original está salvo.
            path_final (str): caminho até a pasta ondes os arquivos derivados das tabelas do arquivo original serão salvos.
        """

        self.path_inicio = path_inicio
        self.path_final = path_final
        os.makedirs(self.path_final, exist_ok=True)

    def saveTable(self, df, fileName, cols):
        """
        Salva uma tabela na pasta de destino

        Args:
           df (DataFrame): DataFrame da tabela que será salva
           fileName (str): nome do arquivo que salvará a tabela
           cols (list): nomes das colunas da tabela
        """

        df = transfColInt(df)
        df.to_csv(self.path_final + fileName, header=cols, index=False)

    def generaterTables(self):
        """
        Gera as tabelas do PNE 2050
        """

        dic_sim = {
            1: "1. Estagnação",
            2: "2. Matriz Elétrica com expansão 100% renovável",
            3: "3. Matriz Elétrica com expansão a partir de tecnologias não emissoras de GEE",
            4: "4. Potencial Hidrelétrico Inventariado sem áreas de interferência",
            5: "5. Efeitos das Mudanças Climáticas (redução de disponibilidade hídrica)",
            6: "6. Efeitos das Mudanças Climáticas (redução de disponibilidade hídrica) sem emissões",
            7: "7. Sobrecusto de 100% no CAPEX de PCH",
            8: "8. Repotenciação de UHE",
            9: "9. Integração Elétrica com países da América do Sul",
            10: "10. Integração Elétrica com países da América do Sul com custo do sistema de transmissão 50% maior",
            11: "11. Integração Elétrica com países da América do Sul com custo do sistema de transmissão 50% menor",
            12: "12. Frota de veículos leves integralmente elétrica em 2050",
            13: "13. Capacidade Instalada Total de Eólica limitada a 50 GW no horizonte",
            14: "14. Capacidade Instalada Total de Eólica e de PV Solar limitada a 50 GW (cada uma) no horizonte",
            15: "15. Eólica Offshore com 20% de redução de CAPEX",
            16: "16. Capacidade Instalada Total de PV Solar limitada a 50 GW (cada uma) no horizonte",
            17: "17. Aumento do fator de capacidade das usinas a bagaço usando insumo com custo na entressafra",
            18: "18. Aumento do fator de capacidade das usinas a bagaço usando insumo com custo 50% maior na entressafra",
            19: "19. Repotenciação e aumento do fator de capacidade das usinas a bagaço usando insumo com custo na entressafra",
            20: "20. Redução de 45% no CAPEX de Usina Nuclear",
            21: "21. Redução de 50% no CAPEX de Usina Nuclear",
            22: "22. Redução de 45% no CAPEX e no OPEX de Usina Nuclear",
            23: "23. Redução de 50% no CAPEX e no OPEX de Usina Nuclear",
            24: "24. Expansão de 8.000 MW de Usinas Nucleares",
            25: "25. Expansão de 10.000 MW de Usinas Nucleares",
            26: "26. Carvão financiado com redução de 20% no CAPEX",
            27: "27. Capacidade Instalada de GD alcança 75 GW em 2050",
            28: "28. Capacidade Instalada de GD limitada a 25 GW em 2050",
            29: "29. GN Pré-Sal ao preço de US$ 6/MMBtu",
            30: "30. Potencial Inventariado Total exceto UHEs em áreas de interferência com Unidades de Conservação (UC)",
            31: "31. Potencial Inventariado Total exceto UHEs em áreas de interferência com Terras Indígenas e Quilombolas (TI)",
            32: "32. UHEs em áreas de interferência com CAPEX dobrado",
            33: "33. UHEs em áreas de interferência com Terras Indígenas e Quilombolas (TI) com CAPEX dobrado",
            34: "34. UHEs em áreas de interferência com Unidades de Conservação (UC) com CAPEX dobrado",
            35: "35. UHEs com interferência após 2040",
            36: "36. Estagnação",
            37: "37. Matriz Elétrica com expansão 100% renovável",
            38: "38. Matriz Elétrica com expansão a partir de tecnologias não emissoras de GEE",
            39: "39. Potencial Hidrelétrico Inventariado com áreas de interferência",
            40: "40. Efeitos das Mudanças Climáticas (redução de disponibilidade hídrica)",
            41: "41. Efeitos das Mudanças Climáticas (redução de disponibilidade hídrica) sem emissões",
            42: "42. Sobrecusto de 100% no CAPEX de PCH",
            43: "43. Repotenciação de UHE",
            44: "44. Integração Elétrica com países da América do Sul",
            45: "45. Integração Elétrica com países da América do Sul com custo do sistema de transmissão 50% maior",
            46: "46. Integração Elétrica com países da América do Sul com custo do sistema de transmissão 50% menor",
            47: "47. Frota de veículos leves integralmente elétrica em 2050",
            48: "48. Capacidade Instalada Total de Eólica limitada a 50 GW no horizonte",
            49: "49. Capacidade Instalada Total de Eólica e de PV Solar limitada a 50 GW (cada uma) no horizonte",
            50: "50. Eólica Offshore com 20% de redução de CAPEX",
            51: "51. Capacidade Instalada Total de PV Solar limitada a 50 GW (cada uma) no horizonte",
            52: "52. Aumento do fator de capacidade das usinas a bagaço usando insumo com custo na entressafra",
            53: "53. Aumento do fator de capacidade das usinas a bagaço usando insumo com custo 50% maior na entressafra",
            54: "54. Repotenciação e aumento do fator de capacidade das usinas a bagaço usando insumo com custo na entressafra",
            55: "55. Redução de 45% no CAPEX de Usina Nuclear",
            56: "56. Redução de 50% no CAPEX de Usina Nuclear",
            57: "57. Redução de 45% no CAPEX e no OPEX de Usina Nuclear",
            58: "58. Redução de 50% no CAPEX e no OPEX de Usina Nuclear",
            59: "59. Expansão de 8.000 MW de Usinas Nucleares",
            60: "60. Expansão de 10.000 MW de Usinas Nucleares",
            61: "61. Carvão financiado com redução de 20% no CAPEX",
            62: "62. Capacidade Instalada de GD alcança 75 GW em 2050",
            63: "63. Capacidade Instalada de GD limitada a 25 GW em 2050",
            64: "64. GN Pré-Sal ao preço de US$ 6/MMBtu"}
        lista = [a[2] for a in os.walk(self.path_inicio)]
        df_pot_acum = pd.DataFrame()
        df_ger_per_med = pd.DataFrame()
        df_atend_ponta = pd.DataFrame()
        df_em_totais = pd.DataFrame()
        df_custo_total = pd.DataFrame()
        df_cons_gas_nat = pd.DataFrame()
        try:
            for arquivo in lista[0]:
                for sheet_name, df in pd.read_excel(self.path_inicio + arquivo, sheet_name=None, header=None).items():
                    if sheet_name == "ResumoDécadas_comGD":
                        arquivo = dic_sim[int(arquivo[0]) * 10 + int(arquivo[1])]
                        df.drop(df.columns[0:1], axis=1, inplace=True)
                        df = df[df.columns[:5]]
                        df_aux = formatTable(df, 33, 44, arquivo)
                        df_pot_acum = pd.concat([df_pot_acum, df_aux])
                        df_aux = formatTable(df, 121, 132, arquivo)
                        df_ger_per_med = pd.concat([df_ger_per_med, df_aux])
                        df_aux = formatTable(df, 155, 166, arquivo)
                        df_atend_ponta = pd.concat([df_atend_ponta, df_aux])
                        df_aux = formatTable(df, 170, 172, arquivo)
                        df_em_totais = pd.concat([df_em_totais, df_aux])
                        df_aux = formatTable(df, 176, 178, arquivo)
                        df_cons_gas_nat = pd.concat([df_cons_gas_nat, df_aux])
                        df.drop(df.columns[3:], axis=1, inplace=True)
                        df_aux = formatTable(df, 185, 187, arquivo)
                        df_aux.iloc[0, 0] = "Expansão Centralizada"
                        df_aux.iloc[1, 0] = "Expansão por GD"
                        df_custo_total = pd.concat([df_custo_total, df_aux])
                        break
            cols = ["Fonte/Tecnologia", "Ano 2015", "Ano 2030", "Ano 2040", "Ano 2050", "Cenário"]
            for c in df_pot_acum.columns:
                if df_pot_acum[c].dtype == 'float64':
                    df_pot_acum[c] = df_pot_acum[c].astype('int64')
            self.saveTable(df_pot_acum, 'PotAcumPNE.csv', cols)
            for c in df_ger_per_med.columns:
                if df_ger_per_med[c].dtype == 'float64':
                    df_ger_per_med[c] = df_ger_per_med[c].astype('int64')
            self.saveTable(df_ger_per_med, 'GerPerMedPNE.csv', cols)
            print("Atend Ponta")
            for c in df_atend_ponta.columns:
                if df_atend_ponta[c].dtype == 'float64':
                    df_atend_ponta[c] = df_atend_ponta[c].astype('int64')
            self.saveTable(df_atend_ponta, 'AtendPontaPNE.csv', cols)
            cols = ["Período", "Ano 2015", "Ano 2030", "Ano 2040", "Ano 2050", "Cenário"]
            for c in df_em_totais.columns:
                if df_em_totais[c].dtype == 'float64':
                    df_em_totais[c] = df_em_totais[c].astype('int64')
            self.saveTable(df_em_totais, 'EmTotPNE.csv', cols)
            for c in df_cons_gas_nat.columns:
                if df_cons_gas_nat[c].dtype == 'float64':
                    df_cons_gas_nat[c] = df_cons_gas_nat[c].astype('int64')
            self.saveTable(df_cons_gas_nat, 'ConsGasNatPNE.csv', cols)
            cols = ["Tipo Expansão", "Ano 2012", "Ano 2015", "Cenário"]
            for c in df_custo_total.columns:
                if df_custo_total[c].dtype == 'float64':
                    df_custo_total[c] = df_custo_total[c].astype('int64')
            self.saveTable(df_custo_total, 'CustoTotPNE.csv', cols)
            return True
        except Exception:
            return False
