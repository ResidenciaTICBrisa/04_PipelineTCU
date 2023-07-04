import pandas as pd
#link da planilha https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/cgcl/clima/arquivos/arquivos_bi/4cn_1990-2016_energia.xlsx
import pathlib

path = pathlib.Path(__file__).parent.resolve()
path = str(path)[0:-15]
path += "/constants/4cn_1990-2016_energia.xlsx"
for sheet_name, df in pd.read_excel(path, sheet_name=None, header=5).items():
    #df = df.drop(range(0,5))
    print(sheet_name)
    print(df)
    #df.to_csv(f'{sheet_name}.csv', encoding='utf-8')