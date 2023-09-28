from pathlib import Path
import pandas as pd
import math
import os

def formataSalvaTabela(df, nome_tab, cols):
    df_final = pd.DataFrame()
    ind_col = 1
    while ind_col < len(df.columns):
        df_aux = df.iloc[1:, 0:1]
        num_rows = len(df_aux)
        new_column_data = [df.iloc[0, ind_col]] * num_rows
        df_aux['Ano'] = new_column_data
        df_aux['Geracao'] = df.iloc[1:,ind_col]
        df_final = pd.concat([df_final, df_aux])
        ind_col += 1   
    df_final['Ano'] = df_final['Ano'].astype('int64')
    df_final.to_csv(path + nome_tab, header=cols, index=False)

def tabelasCapGerEm(df, apaga_ultimo, e_inteiro, apaga_prim):
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
        df.iloc[:, 1:] = df.iloc[:, 1:].applymap(lambda x : math.floor(x) if (x*10 - int(x)*10) < 5 else math.ceil(x))
        for c in df.columns:
            if df[c].dtype ==  'float64':
                df[c] = df[c].astype('int64') 
    return df

def tabelasConsRegioes(df, regioes, apaga_primeiros):
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

if __name__ == '__main__' : 
    arquivo = "Anuario.xlsx" 
    path = str(Path(__file__).parent.resolve()) 
    path += "/constants/" 
    n_tabelas = 0
    cols1 = ["Pais", "Ano","Cap_Inst"]
    cols2 = ["Pais", "Ano","Geracao"]
    cols3 = ["Fonte", "Ano","Cap_Inst"]
    cols4 = ["Fonte", "Ano","Geracao"]
    cols5 = ["Fonte", "Ano","Emissoes"]
    cols6 = ["Subsistema", "Ano","Emissoes"]
    for sheet_name, df in pd.read_excel(path + arquivo, sheet_name=None).items():
        try:
            if n_tabelas == 22:
                break
            df.drop('Unnamed: 0', axis=1, inplace=True)
            if df.iloc[5, 0].find("Capacidade instalada de geração renovável no mundo – 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df,'CapInstRenPaises(GW).csv', cols1)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Capacidade instalada de geração nuclear no mundo - 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df,'CapInstNucPaises(GW).csv', cols1)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Capacidade instalada de geração térmica fóssil no mundo – 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'CapInstTermFosPaises(GW).csv', cols1)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Capacidade instalada de geração hidrelétrica no mundo - 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'CapInstHidPaises(GW).csv', cols1)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Capacidade instalada de geração eólica no mundo - 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'CapInstEolPaises(GW).csv', cols1)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Capacidade instalada de geração solar no mundo - 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'CapInstSolPaises(GW).csv', cols1)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Capacidade instalada de geração biomassa no mundo - 10 maiores países") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'CapInstBioPaises(GW).csv', cols1)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Geração renovável no mundo – 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'GerRenPaises(TWh).csv', cols2)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Geração nuclear no mundo - 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'GerNucPaises(TWh).csv', cols2)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Geração térmica fóssil no mundo – 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'GerTermFosPaises(TWh).csv', cols2)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Geração hidrelétrica no mundo ") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'GerHidPaises(TWh).csv', cols2)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Geração eólica no mundo - 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'GerEolPaises(TWh).csv', cols2)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Geração solar no mundo - 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'GerSolPaises(TWh).csv', cols2)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Geração biomassa no mundo - 10 maiores") != -1:
                df = tabelasCapGerEm(df, True, True, True)
                formataSalvaTabela(df, 'GerBioPaises(TWh).csv', cols2)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Capacidade instalada de geração elétrica no Brasil (MW)") != -1:
                df = tabelasCapGerEm(df, False, True, True)
                formataSalvaTabela(df, 'CapInstFonte(MW).csv', cols3)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Geração elétrica por fonte no Brasil (GWh)") != -1:
                df = tabelasCapGerEm(df, False, True, True)
                formataSalvaTabela(df, 'GelElFonte(GWh).csv', cols4)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Emissões de GEE no SIN - MtCO2") != -1:
                df = tabelasCapGerEm(df, False, False, True)
                formataSalvaTabela(df, 'EmGEESIN(MtCO2).csv', cols5)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Emissões de GEE no Sistema Isolado - MtCO2") != -1:
                df = tabelasCapGerEm(df, False, False, True)
                formataSalvaTabela(df, 'EmGEESistIso(MtCO2).csv', cols5)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Emissões de GEE provenientes da Geração Elétrica no Brasil - MtCO2") != -1:
                df = tabelasCapGerEm(df, False, False, True)
                formataSalvaTabela(df, 'EmGEEGerEl(MtCO2).csv', cols6)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Consumo médio total por subsistema, região e UF") != -1:
                regioes = ["Norte","Nordeste","Sudeste","Sul", "Centro-Oeste", "Regiões geográficas"]
                cols7 = ["Subsistema", "Ano","Cons_Med_Tot"]
                cols8 = ["Regiao", "Ano","Cons_Med_Tot"]
                df = tabelasCapGerEm(df, False, False, True)
                formataSalvaTabela(df.iloc[0:7,:], 'ConsMedTotSubsis(kWh_mes).csv', cols7)
                df = tabelasConsRegioes(df, regioes, True)
                formataSalvaTabela(df,'ConsMedTotReg(kWh_mes).csv', cols8)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Consumo médio residencial por subsistema, região e UF") != -1:
                regioes = ["Norte","Nordeste","Sudeste","Sul", "Centro-Oeste", "Regiões geográficas"]
                cols7 = ["Subsistema", "Ano","Cons_Med_Res"]
                cols8 = ["Regiao", "Ano","Cons_Med_Res"]
                df = tabelasCapGerEm(df, False, False,True)
                formataSalvaTabela(df.iloc[0:7,:], 'ConsMedResSubsis(kWh_mes).csv', cols7)
                df = tabelasConsRegioes(df, regioes, True)
                formataSalvaTabela(df,'ConsMedResReg(kWh_mes).csv', cols8)
                n_tabelas += 1
            elif df.iloc[5, 0].find("Consumo médio anual per capita por região e UF (kWh/hab)") != -1:
                regioes = ["Norte","Nordeste","Sudeste","Sul", "Centro-Oeste", "Brasil"]
                cols8 = ["Regiao", "Ano","Cons_Med_An_PC"]
                df = tabelasCapGerEm(df, False, False, False)
                df = tabelasConsRegioes(df, regioes, False)
                formataSalvaTabela(df,'ConsMedAnPerCapReg(kWh_hab).csv', cols8)
                n_tabelas += 1
        except Exception as e:
            continue