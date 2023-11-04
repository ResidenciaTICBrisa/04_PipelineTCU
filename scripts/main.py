from datetime import datetime
import pathlib
from handlers.anuarioANPHandler import AnuarioANPHandler
from handlers.anuarioHandler import AnuarioHandler
from handlers.benHandler import BenHandler
from handlers.comunicacaoHandler import ComunicacaoHandler
from handlers.pcbioHandler import PCBIOHandler
from handlers.pneHandler import PNEHandler
from handlers.ieaHandler import IeaHandler
from scrappers.excelScrapper import ExcelScrapper
from scrappers.excelScrapperByHref import ExcelScrapperByHref
from scrappers.excelScrapperAnuarioANP import ExcelScrapperAnuarioANP
from scrappers.zipScrapper import ZipScrapper
from scrappers.excelScrapperIEA import ExcelScrapperIEA

if __name__ == '__main__':
    year_atual = datetime.now().year
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_consts = path_dir + '/constants/'
    path_raiz = path_dir[0:-7]
    path_const_input = path_consts + 'Anuario Estatistico Energia Eletrica Input/'
    path_const_output = path_consts + 'Anuario Estatistico Energia Eletrica Output/'
    name_left = 'Anuário'
    year = year_atual
    name_right = 'Workbook'
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/anuario-estatistico-de-energia-eletrica'
    url_final = 'https://www.epe.gov.br'
    file = 'Anuario.xlsx'
    cont = 0
    while cont < 10:
        scrapper = ExcelScrapper(name_left, str(year), name_right, url_site, url_final, file, path_raiz, path_const_input)
        if scrapper.getLink() is not None:
            if scrapper.getFile():
                anuario = AnuarioHandler(file, path_const_input, path_const_output)
                anuario.generateTables()
                break
        year -= 1
        cont += 1

    path_const_input = path_consts + 'BEN Input/'
    path_const_output = path_consts + 'BEN Output/'
    name_left = 'Matrizes Consolidadas'
    year = year_atual
    name_right = ''
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/BEN-Series-Historicas-Completas'
    file = 'BEN.xlsx'
    cont = 0
    while cont < 10:
        scrapper = ExcelScrapper(name_left, str(year), name_right, url_site, url_final, file, path_raiz, path_const_input)
        if scrapper.getLink() is not None:
            if scrapper.getFile():
                ben = BenHandler(file, path_const_input, path_const_output)
                ben.generateTable()
                break
        year -= 1
        cont += 1

    path_const_input = path_consts + 'PNE2050 Input/'
    path_const_output = path_consts + 'PNE2050 Output/'
    name_left = 'Relatórios de saída'
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/Plano-Nacional-de-Energia-2050'
    scrapper = ZipScrapper(name_left, url_site, url_final, path_const_input)
    if scrapper.getLink() is not None:
        if scrapper.getFile():
            pne = PNEHandler(path_const_input, path_const_output)
            pne.generaterTables()

    path_const_input = path_consts + 'Comunicacao Nacional Input/'
    path_const_output = path_consts + 'Comunicacao Nacional Output/'
    name_left = 'EmissoesGEE'
    url_site = 'https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/indicadores/paginas/dados-abertos/dados-abertos-mctic/sirene-sistema-de-registro-nacional-de-emissoes'
    file = 'ComunicacaoNacional.xlsx'
    scrapper = ExcelScrapperByHref(name_left, url_site, file, path_raiz, path_const_input)
    if scrapper.getLink() is not None:
        if scrapper.getFile():
            comunicacao = ComunicacaoHandler(file, path_const_input, path_const_output)
            comunicacao.generateTable()

    path_const_input = path_consts + 'PCBIO Input/'
    path_const_output = path_consts + 'PCBIO Output/'
    name_left = 'PCBIO'
    year = year_atual
    url_site = 'https://www.ccee.org.br/web/guest/pre%C3%A7o-m%C3%A9dio-de-descarboniza%C3%A7%C3%A3o-informa%C3%A7%C3%B5es'
    url_final = 'https://www.ccee.org.br'
    file = 'PCBIO.xlsx'
    cont = 0
    while cont < 10:
        scrapper = ExcelScrapperByHref(name_left, url_site, file, path_raiz, path_const_input, str(year), url_final)
        if scrapper.getLink() is not None:
            if scrapper.getFile():
                pcbio = PCBIOHandler(file, path_const_input, path_const_output)
                pcbio.generateTables()
                break
        year -= 1
        cont += 1
    path_const_input = path_consts + 'Anuario ANP Input/'
    path_const_output = path_consts + 'Anuario ANP Output/'
    year = year_atual
    cont = 0
    url_site = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/anuario-estatistico-"
    tab_nomes = [
        "tabela1-6.csv",
        "tabela1-7.csv",
        "tabela1-8.csv",
        "tabela2-9.csv",
        "tabela2-13.csv",
        "tabela2-16.csv",
        "tabela4-1.csv",
        "tabela4-10.csv",
        "tabela4-16.csv",
        "tabela4-17.csv"
    ]
    while cont < 10:
        scrapper = ExcelScrapperAnuarioANP(url_site + str(year), path_raiz, path_const_input)
        if len(scrapper.getLinks()) > 0:
            if scrapper.getFiles(tab_nomes):
                handler = AnuarioANPHandler(path_const_input, path_const_output)
                dic_tab_nomes = {
                    "tabela1-6.csv": ["ResProvGNPaises.csv", 2, "val_res"],
                    "tabela1-7.csv": ["ProdGNPaises.csv", 2, "val_prod"],
                    "tabela1-8.csv": ["ConsGNPaises.csv", 1, "val_cons"]
                }
                handler.generateTablesGN(dic_tab_nomes)
                dic_tab_nomes = {
                    "tabela2-9.csv": ["ProdPetrUF.csv", "prod_pet"],
                    "tabela2-13.csv": ["ProdGNUF.csv", "prod_gn"],
                    "tabela2-16.csv": ["QueimaPerdaGNUF.csv", "queima_perda_pet"]
                }
                handler.generateTablesPetGNNac(dic_tab_nomes)
                dic_tab_nomes = {
                    "tabela4-1.csv": ["ProdEtAniHidUF.csv", "prod_etanol_anidro_hidr"],
                    "tabela4-10.csv": ["ProdB100UF.csv", "prod_biodiesel"]
                }
                handler.generateTablesBioCombs(dic_tab_nomes)
                dic_tab_nomes = {
                    "tabela4-16.csv": ["EmCBIOBioComb.csv", "biocombustivel", "emissao_cbio"],
                    "tabela4-17.csv": ["ApCBIO.csv", "distribuidores_combustivel", "outros_agentes"]
                }
                handler.generateTablesCBIO(dic_tab_nomes, year - 1)
                break
        year -= 1
        cont += 1

    # url_site = "https://www.iea.org/data-and-statistics/data-product/world-energy-statistics-and-balances"
    # scrapperIea = ExcelScrapperIEA(url_site, path_raiz)
    # nome_arquivo = scrapperIea.baixa_arquivo()
    # ieaHandler = IeaHandler(file=nome_arquivo)
    # ieaHandler.formatar_xlsx_IEA()
