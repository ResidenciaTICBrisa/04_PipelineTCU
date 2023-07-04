import pandas as pd
#link da planilha https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/cgcl/clima/arquivos/arquivos_bi/4cn_1990-2016_energia.xlsx
import pathlib

planilhas = [
    "Custo das tecnologias - Baterias.csv",
    "Custo das tecnologias - Eletrolisadores de Hidrogênio.csv",
    "Custo das tecnologias - Equipamento de Capital da Captura e Armazenamento de Carbono (CAC).csv",
    "Custo das tecnologias - Solar Fotovoltaica (Escala de Utilidade.csv",
    "Custo das tecnologias - Turbinas Eólicas Offhore.csv",
    "Custo das tecnologias - Turbinas Eólicas Onshore.csv",
    "Emissões - CO2e - Eletricidade.csv"       
]

path = pathlib.Path(__file__).parent.resolve()
path = str(path)[0:-15]
path += "/constants"
for planilha in planilhas:
    df = pd.read_csv(path + '/' + planilha)
    print(planilha)
    print(df)
    #df.to_csv(f'{sheet_name}.csv', encoding='utf-8')