import pandas as pd
import os
import warnings
import math
import numpy
warnings.filterwarnings("ignore")

def transfColInt(df):
    for c in df.columns:
        if df[c].dtype ==  'float64':
            df[c] = df[c].astype('int64') 
    return df

dic_sim = {
    1 : "1. Estagnação",
    2 : "2. Matriz Elétrica com expansão 100% renovável",
    3 : "3. Matriz Elétrica com expansão a partir de tecnologias não emissoras de GEE",
    4 : "4. Potencial Hidrelétrico Inventariado sem áreas de interferência",
    5 : "5. Efeitos das Mudanças Climáticas (redução de disponibilidade hídrica)",
    6 : "6. Efeitos das Mudanças Climáticas (redução de disponibilidade hídrica) sem emissões",
    7 : "7. Sobrecusto de 100% no CAPEX de PCH",
    8 : "8. Repotenciação de UHE",
    9 : "9. Integração Elétrica com países da América do Sul",
    10 : "10. Integração Elétrica com países da América do Sul com custo do sistema de transmissão 50% maior",
    11 : "11. Integração Elétrica com países da América do Sul com custo do sistema de transmissão 50% menor",
    12 : "12. Frota de veículos leves integralmente elétrica em 2050",
    13 : "13. Capacidade Instalada Total de Eólica limitada a 50 GW no horizonte",
    14 : "14. Capacidade Instalada Total de Eólica e de PV Solar limitada a 50 GW (cada uma) no horizonte",
    15 : "15. Eólica Offshore com 20% de redução de CAPEX",
    16 : "16. Capacidade Instalada Total de PV Solar limitada a 50 GW (cada uma) no horizonte",
    17 : "17. Aumento do fator de capacidade das usinas a bagaço usando insumo com custo na entressafra",
    18 : "18. Aumento do fator de capacidade das usinas a bagaço usando insumo com custo 50% maior na entressafra",
    19 : "19. Repotenciação e aumento do fator de capacidade das usinas a bagaço usando insumo com custo na entressafra",
    20 : "20. Redução de 45% no CAPEX de Usina Nuclear",
    21 : "21. Redução de 50% no CAPEX de Usina Nuclear",
    22 : "22. Redução de 45% no CAPEX e no OPEX de Usina Nuclear",
    23 : "23. Redução de 50% no CAPEX e no OPEX de Usina Nuclear",
    24 : "24. Expansão de 8.000 MW de Usinas Nucleares",
    25 : "25. Expansão de 10.000 MW de Usinas Nucleares",
    26 : "26. Carvão financiado com redução de 20% no CAPEX",
    27 : "27. Capacidade Instalada de GD alcança 75 GW em 2050",
    28 : "28. Capacidade Instalada de GD limitada a 25 GW em 2050",
    29 : "29. GN Pré-Sal ao preço de US$ 6/MMBtu",
    30 : "30. Potencial Inventariado Total exceto UHEs em áreas de interferência com Unidades de Conservação (UC)",
    31 : "31. Potencial Inventariado Total exceto UHEs em áreas de interferência com Terras Indígenas e Quilombolas (TI)",
    32 : "32. UHEs em áreas de interferência com CAPEX dobrado",
    33 : "33. UHEs em áreas de interferência com Terras Indígenas e Quilombolas (TI) com CAPEX dobrado",
    34 : "34. UHEs em áreas de interferência com Unidades de Conservação (UC) com CAPEX dobrado",
    35 : "35. UHEs com interferência após 2040",
    36 : "36. Estagnação",
    37 : "37. Matriz Elétrica com expansão 100% renovável",
    38 : "38. Matriz Elétrica com expansão a partir de tecnologias não emissoras de GEE",
    39 : "39. Potencial Hidrelétrico Inventariado com áreas de interferência",
    40 : "40. Efeitos das Mudanças Climáticas (redução de disponibilidade hídrica)",
    41 : "41. Efeitos das Mudanças Climáticas (redução de disponibilidade hídrica) sem emissões",
    42 : "42. Sobrecusto de 100% no CAPEX de PCH",
    43 : "43. Repotenciação de UHE",
    44 : "44. Integração Elétrica com países da América do Sul",
    45 : "45. Integração Elétrica com países da América do Sul com custo do sistema de transmissão 50% maior",
    46 : "46. Integração Elétrica com países da América do Sul com custo do sistema de transmissão 50% menor",
    47 : "47. Frota de veículos leves integralmente elétrica em 2050",
    48 : "48. Capacidade Instalada Total de Eólica limitada a 50 GW no horizonte",
    49 : "49. Capacidade Instalada Total de Eólica e de PV Solar limitada a 50 GW (cada uma) no horizonte",
    50 : "50. Eólica Offshore com 20% de redução de CAPEX",
    51 : "51. Capacidade Instalada Total de PV Solar limitada a 50 GW (cada uma) no horizonte",
    52 : "52. Aumento do fator de capacidade das usinas a bagaço usando insumo com custo na entressafra",
    53 : "53. Aumento do fator de capacidade das usinas a bagaço usando insumo com custo 50% maior na entressafra",
    54 : "54. Repotenciação e aumento do fator de capacidade das usinas a bagaço usando insumo com custo na entressafra",
    55 : "55. Redução de 45% no CAPEX de Usina Nuclear",
    56 : "56. Redução de 50% no CAPEX de Usina Nuclear",
    57 : "57. Redução de 45% no CAPEX e no OPEX de Usina Nuclear",
    58 : "58. Redução de 50% no CAPEX e no OPEX de Usina Nuclear",
    59 : "59. Expansão de 8.000 MW de Usinas Nucleares",
    60 : "60. Expansão de 10.000 MW de Usinas Nucleares",
    61 : "61. Carvão financiado com redução de 20% no CAPEX",
    62 : "62. Capacidade Instalada de GD alcança 75 GW em 2050",
    63 : "63. Capacidade Instalada de GD limitada a 25 GW em 2050",
    64 : "64. GN Pré-Sal ao preço de US$ 6/MMBtu"
}
                                 
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
                if arquivo[1] >= '0' and arquivo[1] <= '9':
                    indice_dic = int(arquivo[0])*10 + int(arquivo[1])
                else :
                    indice_dic = int(arquivo[0]) 
                arquivo_aux = dic_sim[indice_dic]
                df.drop(df.columns[0:1], axis=1, inplace=True)
                colunas_mantidas = df.columns[:5]
                df = df[colunas_mantidas]
                df_aux = df.iloc[33:44]
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : math.floor(x) if (x*10 - int(x)*10) < 5 else math.ceil(x))
                num_rows = len(df_aux)
                new_column_data = [arquivo_aux] * num_rows
                df_aux['Cenário'] = new_column_data
                df_pot_acum = pd.concat([df_pot_acum, df_aux])
                df_aux = df.iloc[121 : 132]
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : math.floor(x) if (x*10 - int(x)*10) < 5 else math.ceil(x))
                num_rows = len(df_aux)
                new_column_data = [arquivo_aux] * num_rows
                df_aux['Cenário'] = new_column_data
                df_ger_per_med = pd.concat([df_ger_per_med, df_aux])
                df_aux = df.iloc[155 : 166]
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : math.floor(x) if (x*10 - int(x)*10) < 5 else math.ceil(x))
                num_rows = len(df_aux)
                new_column_data = [arquivo_aux] * num_rows
                df_aux['Cenário'] = new_column_data
                df_atend_ponta = pd.concat([df_atend_ponta, df_aux])
                df_aux = df.iloc[170 : 172]
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : math.floor(x) if (x*10 - int(x)*10) < 5 else math.ceil(x))
                num_rows = len(df_aux)
                new_column_data = [arquivo_aux] * num_rows
                df_aux['Cenário'] = new_column_data
                df_em_totais = pd.concat([df_em_totais, df_aux])
                df_aux = df.iloc[176:178]
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : math.floor(x) if (x*10 - int(x)*10) < 5 else math.ceil(x))
                num_rows = len(df_aux)
                new_column_data = [arquivo_aux] * num_rows
                df_aux['Cenário'] = new_column_data
                df_cons_gas_nat = pd.concat([df_cons_gas_nat, df_aux])
                df_aux = df.iloc[185:187]
                df_aux.drop(df.columns[3:], axis=1, inplace=True)
                df_aux.iloc[:, 1:] = df_aux.iloc[:, 1:].applymap(lambda x : math.floor(x) if (x*10 - int(x)*10) < 5 else math.ceil(x))
                num_rows = len(df_aux)
                df_aux.iloc[0, 0] = "Expansão Centralizada"
                df_aux.iloc[1, 0] = "Expansão por GD"
                new_column_data = [arquivo_aux] * num_rows
                df_aux['Cenário'] = new_column_data
                df_custo_total = pd.concat([df_custo_total, df_aux])
                num_rows = len(df_aux)
                new_column_data = [arquivo_aux] * num_rows
                df_aux['Cenário'] = new_column_data
                break
    if not os.path.exists(cenarios):
        os.makedirs(cenarios)
    df_pot_acum = transfColInt(df_pot_acum)
    df_pot_acum.to_csv(cenarios + 'PotAcumPNE.csv', header=cols1, index=False) 
    df_ger_per_med = transfColInt(df_ger_per_med)
    df_ger_per_med.to_csv(cenarios + 'GerPerMedPNE.csv', header=cols1, index=False)
    df_atend_ponta = transfColInt(df_atend_ponta)
    df_atend_ponta.to_csv(cenarios + 'AtendPontaPNE.csv', header=cols1, index=False)
    df_em_totais = transfColInt(df_em_totais)
    df_em_totais.to_csv(cenarios + 'EmTotPNE.csv', header=cols2, index=False)
    df_custo_total = transfColInt(df_custo_total)
    df_custo_total.to_csv(cenarios + 'CustoTotPNE.csv', header=cols3, index=False)
    df_cons_gas_nat = transfColInt(df_cons_gas_nat)
    df_cons_gas_nat.to_csv(cenarios + 'ConsGasNatPNE.csv', header=cols2, index=False)