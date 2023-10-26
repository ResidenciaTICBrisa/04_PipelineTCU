import pathlib

from Scrappers.excelScrapperIEA import ExcelScrapperIEA


url = 'https://www.iea.org/data-and-statistics/data-product/world-energy-statistics-and-balances'
path_raiz = str(pathlib.Path(__file__).parent.resolve())
if __name__ == '__main__':
    print(path_raiz)
    scrapperIEA = ExcelScrapperIEA(url,path_raiz=path_raiz)
    if scrapperIEA.baixa_arquivo():
        print(f"Arquivo {scrapperIEA.nome_arquivo} baixado! ")
    else:
        print("Não foi possivel baixar o arquivo")