from anuarioHandler import AnuarioHandler
from datetime import datetime
from excelScrapper import ExcelScrapper

if __name__ == '__main__':
    name_left = 'Anuário'
    year = datetime.now().year
    name_right = 'Workbook'
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/anuario-estatistico-de-energia-eletrica'
    url_final = 'https://www.epe.gov.br'
    file = 'Anuario.xlsx'
    cont = 0
    while(cont < 10):
        scrapper = ExcelScrapper(name_left, str(year), name_right, url_site, url_final, file)
        if scrapper.link != None:
            sub_path = '/constants/'
            if scrapper.getFile(sub_path):
                anuario = AnuarioHandler(file)
                anuario.generateTables()
                break
        year -= 1
        cont += 1