from pathlib import Path
import pandas as pd


class IeaHandler:
    """
    Classe responsável por ler um arquivo correspondente ao Energy Statics Data Browser do IEA, seleciona e salva
    as tabelas desejadas e salva em um arquivo csv
    Atributos:
    file (str): nome do arquivo que será lido
    n_tabelas (str): número de tabelas que o arquivo conseguiu criar, inicialmente é zero
    path (str): caminho até a pasta onde os arquivos serão salvos
    paises (str): lista de paises que estão na base de dados da IEA
    """
    def __init__(self, file) -> None:
        """

        :param file:
        """
        self.file = file
        self.n_table = 0
        self.tables = []
        self.path = str(Path(__file__).parent.resolve())
        self.paises = [
            "Argentina",
            "Australia",
            "Austria",
            "Belgium",
            "Brazil",
            "Canada",
            "Chile",
            "China",
            "Colombia",
            "Czech Republic",
            "Denmark",
            "Egypt",
            "Estonia",
            "Finland",
            "France",
            "Germany",
            "Greece",
            "Hungary",
            "India",
            "Indonesia",
            "Ireland",
            "Israel",
            "Italy",
            "Japan",
            "Kenya",
            "Korea",
            "Latvia",
            "Lithuania",
            "Luxembourg",
            "Mexico",
            "Morocco",
            "New Zealand",
            "Norway",
            "Poland",
            "Portugal",
            "Senegal",
            "Singapore",
            "Slovak Republic",
            "South Africa",
            "Spain",
            "Sweden",
            "Switzerland",
            "The Netherlands",
            "Thailand",
            "Türkiye",
            "Ukraine",
            "United Kingdom",
            "United States"
        ]
        # TODO: Será necessário fazer métodos que irão ler o arquivo xlsx e direcionar para a página certa da planilha
        # TODO: Será necessário fazer um método que, ao ler o arquivo xlsx, selecionará as linhas que possuem a coluna de flow igual a Total energy supply (PJ) e a coluna de country correspondente aos países citados na lista de paises

    def formatar_xlsx_IEA(self) -> None:
        """
        Função responsável por ler o arquivo excel, selecionar o sheet específico e salvar apenas as informações
        importantes em um novo arquivo do tipo csv.
        :param nome_tab:
        :return: bool
        """
        excel_file = pd.ExcelFile(self.path + "/constants/IEA/" + self.file)
        df_iea_sheet_principal = pd.read_excel(excel_file, sheet_name=3)
        lista_indices_linhas = df_iea_sheet_principal.index[df_iea_sheet_principal.iloc[:, 2] == 'Total energy supply ' '(PJ)'].tolist()
        df_novo_csv = df_iea_sheet_principal.iloc[lista_indices_linhas]
        nome_colunas_novas = ['PAIS', 'PRODUTO', 'DADO_TIPO']
        df_novo_csv.columns.values[:3] = nome_colunas_novas

        df_novo_csv = df_novo_csv.drop(df_novo_csv.columns[3:6], axis=1)

        df_novo_csv.columns.values[3:] = df_iea_sheet_principal.iloc[0, 6:]

        df_novo_csv.replace('..', 0, inplace=True)

        df_novo_csv.to_csv(self.path + "/constants/IEA/" + "tabelas_paises_TES.csv", index=False)
