import pandas as pd
import pathlib

path = pathlib.Path(__file__).parent.resolve()
path = str(path)[0:-15]
path += "/constants/Matriz ab2022 site.xlsx"
for sheet_name, df in pd.read_excel(path, sheet_name=None).items():
    print(sheet_name)
    print(df)