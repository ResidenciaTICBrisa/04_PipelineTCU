from pathlib import Path
import pandas as pd
import numpy as np

if __name__ == '__main__' : 
    arquivo = "BEN.xlsx" 
    path = str(Path(__file__).parent.resolve()) 
    path += "/constants/" 
    ano = 2022
    totais = []
    for sheet_name, df in pd.read_excel(path + arquivo, sheet_name=None).items():
        if ano < 2018:
            break
        df.drop('Unnamed: 0', axis=1, inplace=True)
        i = 0
        df.fillna(0, inplace=True)
        while True:
            if isinstance(df.iloc[0,0], str): 
                if df.iloc[0,0].find('CONSUMO FINAL') != -1:
                    break
            df.drop(i, axis=0, inplace=True)
            i += 1
        i += 1
        df.drop('Unnamed: 1', axis=1, inplace=True)
        try:
            while True:
                df.drop(i, axis=0, inplace=True)
                i += 1
        except:    
            #OLEO DIESEL = DIESEL DE PETROLEO
            #GAS DE COQUEIRA = GAS DE CIDADE E DE COQUERIA 
            #COQUE DE PETROLEO APAGADO 
            #OUTROS ENERGETICOS DE PETROLEO = OUTRAS SECUNDARIAS DE PETRÓLEO 
            coeficientes = {
                "PETROLEO" : 3.04,
                "GAS NATURAL" : 2.34,
                "CARVAO VAPOR" : 3.882,
                "CARVAO METALURGICO" : 3.882,
                "OLEO DIESEL" : 3.07,
                "OLEO COMBUSTIVEL" : 3.18,
                "GASOLINA" : 2.873,
                "GLP" : 2.614,
                "NAFTA" : 3.04,
                "QUEROSENE" : 2.964,
                "GAS DE COQUERIA" : 1.81,
                "COQUE DE CARVAO MINERAL" : 4.38250259931927,
                "OUTROS ENERGETICOS DE PETROLEO" : 3.04,
                "ALCATRAO" : 3.344
            }
            rotulos_nov = ["PETROLEO","GAS NATURAL","CARVAO VAPOR", "CARVAO METALURGICO", "URANIO U3O8", "ENERGIA HIDRAULICA", "LENHA", "PRODUTOS DA CANA", "OUTRAS FONTES PRIMARIAS", "ENERGIA PRIMARIA TOTAL", "BIODIESEL", "OLEO DIESEL", "OLEO COMBUSTIVEL", "GASOLINA", "GLP", "NAFTA", "QUEROSENE", "GAS DE COQUERIA", "COQUE DE CARVAO MINERAL", 	 "URANIO CONTIDO NO UO2", "ELETRICIDADE", "CARVAO VEGETAL", "ALCOOL ETILICO ANIDRO E HIDRATADO", "OUTROS ENERGETICOS DE PETROLEO", "PRODUTOS NAO ENERGETICOS DE PETROLEO", "ALCATRAO", "ENERGIA SECUNDARIA TOTAL", "TOTAL"]
            rotulos_ant = []
            for j in range(2, 30):
                col = 'Unnamed: ' + str(j)
                rotulos_ant.append(col)
            ren = {rotulos_ant[j]: rotulos_nov[j] for j in range(len(rotulos_ant))}
            df.rename(columns=ren, inplace=True)
            apagar = ["URANIO U3O8","ENERGIA HIDRAULICA", "LENHA", "PRODUTOS DA CANA", "OUTRAS FONTES PRIMARIAS", "ENERGIA PRIMARIA TOTAL", "BIODIESEL", "URANIO CONTIDO NO UO2", "ELETRICIDADE", "CARVAO VEGETAL", "ALCOOL ETILICO ANIDRO E HIDRATADO", "PRODUTOS NAO ENERGETICOS DE PETROLEO","ENERGIA SECUNDARIA TOTAL", "TOTAL"]
            mantidas = ["PETROLEO","GAS NATURAL","CARVAO VAPOR", "CARVAO METALURGICO", "OLEO DIESEL", "OLEO COMBUSTIVEL", "GASOLINA", "GLP", "NAFTA", "QUEROSENE", "GAS DE COQUERIA", "COQUE DE CARVAO MINERAL", "OUTROS ENERGETICOS DE PETROLEO", "ALCATRAO"]
            df.drop(apagar, axis = 1, inplace=True)
            for m in mantidas:
                df[m].iloc[0] = df[m].iloc[0]*coeficientes[m]
            total = 0
            for a in range(0, len(df.iloc[0])):
                total += df.iloc[0, a]
            totais.append(total)
            ano -= 1
    totais.reverse()
    df_totais = pd.DataFrame(np.array(totais), range(2018, 2023), ['T'])  
    df_totais.to_csv(path + "Emissoes_Totais_BEN.csv")  
