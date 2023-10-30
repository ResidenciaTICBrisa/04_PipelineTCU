from datetime import datetime
import pathlib
from ..handlers.pcbioHandler import PCBIOHandler
from ..scrappers.excelScrapperByHref import ExcelScrapperByHref


def teste_getPCBIO():
    """
    Testa se o código baixa o arquivo desejado e baixa as tabelas

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    year_atual = datetime.now().year
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_raiz = path_dir[0:-7]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste PCBIO Input/'
    path_const_output = path_consts + 'Teste PCBIO Output/'
    name_left = 'PCBIO'
    year = year_atual
    url_site = 'https://www.ccee.org.br/web/guest/pre%C3%A7o-m%C3%A9dio-de-descarboniza%C3%A7%C3%A3o-informa%C3%A7%C3%B5es'
    url_final = 'https://www.ccee.org.br'
    file = 'PCBIO.xlsx'
    scrapper = ExcelScrapperByHref(name_left, url_site, file, path_raiz, path_const_input, str(year), url_final)
    pcbio = PCBIOHandler(file, path_const_input, path_const_output)
    if scrapper.getLink() is not None:
        scrapper.getFile()
        assert pcbio.generateTables()
    else:
        year -= 1
        scrapper = ExcelScrapperByHref(name_left, url_site, file, path_raiz, path_const_input, str(year), url_final)
        scrapper.getFile()
        assert pcbio.generateTables()


def teste_getPCBIO_pathErrado():
    """
    Testa se o código detecta um erro quando fornecemos um caminho de origem errado

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste PCBIO Input Errado/'
    path_const_output = path_consts + 'Teste PCBIO Output/'
    file = 'PCBIO.xlsx'
    pcbio = PCBIOHandler(file, path_const_input, path_const_output)
    assert not pcbio.generateTables()
