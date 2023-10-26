import pandas as pd
from pathlib import Path


class IeaHandler:
    # Classe responsável por ler um arquivo correspondente ao Energy Statics Data Browser do IEA, seleciona e salva
    # as tabelas desejadas e salva em um arquivo csv
    # Atributos:
    # file (str): nome do arquivo que será lido
    # n_tabelas (str): número de tabelas que o arquivo conseguiu criar, inicialmente é zero
    # path (str): caminho até a pasta onde os arquivos serão salvos
    # paises (str): lista de paises que estão na base de dados da IEA

    def __init__(self, file) -> None:
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
