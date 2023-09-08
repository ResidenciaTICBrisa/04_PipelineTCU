from pathlib import Path
import pandas as pd
import numpy as np
import pytest
def converter_float_para_inteiro(df):
    pytest.set_trace()
    df.iloc[1:,1:-1]=df.iloc[1:,1:-1].astype('int')  
    return df

if __name__ == '__main__' : 
    arquivo = "BEN.xlsx" 
    path = str(Path(__file__).parent.resolve()) 
    path += "/constants/" 
    cont = False
    df_total = pd.DataFrame()
    for sheet_name, df in pd.read_excel(path + arquivo, sheet_name=None).items():
        df.drop('Unnamed: 0', axis=1, inplace=True)
        df.dropna(inplace=True)
        i = 0
        while len(df.index) != 19:
            titulo = df.iloc[i,0].replace(' ', '')
            if titulo == 'CONTA':
                i += 1
            elif titulo == 'PRODUÇÃO':
                i += 1
            elif titulo == 'IMPORTAÇÃO':
                i += 1
            elif titulo == 'VARIAÇÃODEESTOQUES':
                df.iloc[i,0] = 'VARIAÇÃO DE ESTOQUES'
                i += 1
            elif titulo == 'EXPORTAÇÃO':
                i += 1
            elif titulo == 'NÃO-APROVEITADA':
                i += 1
            elif titulo == 'REINJEÇÃO':
                i += 1
            elif titulo == 'CONSUMOFINALNÃO-ENERGÉTICO':
                df.iloc[i,0] = 'CONSUMO FINAL NÃO-ENERGÉTICO'
                i += 1
            elif titulo == 'SETORENERGÉTICO':
                df.iloc[i,0] = 'SETOR ENERGÉTICO'
                i += 1   
            elif titulo == 'RESIDENCIAL':
                i += 1   
            elif titulo == 'COMERCIAL':
                i += 1   
            elif titulo == 'PÚBLICO':
                i += 1   
            elif titulo == 'AGROPECUÁRIO':
                i += 1   
            elif titulo== 'RODOVIÁRIO':
                i += 1 
            elif titulo == 'FERROVIÁRIO':
                i += 1 
            elif titulo == 'AÉREO':
                i += 1   
            elif titulo == 'HIDROVIÁRIO':
                i += 1   
            elif titulo == 'INDUSTRIAL-TOTAL':
                i += 1   
            elif titulo == 'CONSUMONÃO-IDENTIFICADO':
                df.iloc[i,0] = 'CONSUMO NÃO-IDENTIFICADO'
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
        df_total = pd.concat([df_total,df])
    df_total=converter_float_para_inteiro(df_total)
    df_total.to_csv(path + "BEN_total.csv", index=False, header=False) 
