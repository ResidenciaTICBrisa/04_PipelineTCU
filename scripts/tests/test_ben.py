import pathlib
from datetime import datetime
from ..handlers.benHandler import BenHandler
from ..scrappers.excelScrapper import ExcelScrapper


def teste_getBEN():
    """
    Testa se o código pega o arquivo das Matrizes Consolidadas do BEN de no máximo no ano passado

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    year = datetime.now().year
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_raiz = path_dir[0:-7]
    path_const_input = path_consts + 'Teste BEN Input/'
    name_left = 'Matrizes Consolidadas'
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/BEN-Series-Historicas-Completas'
    url_final = 'https://www.epe.gov.br'
    file = 'BEN.xlsx'
    scrapper = ExcelScrapper(name_left, str(year), '', url_site, url_final, file, path_raiz, path_const_input)
    if scrapper.getLink() is not None:
        assert scrapper.getFile()
    else:
        year -= 1
        scrapper = ExcelScrapper(name_left, str(year), '', url_site, url_final, file, path_raiz, path_const_input)
        assert scrapper.getFile()


# def teste_getTablesBEN():
#     """
#     Testa se o código pega o arquivo original, trata e cria o arquivo desejado

#     Retorna:
#         assert (bool): O método retorna o resultado da comparação.
#     """
#     path_dir = str(pathlib.Path(__file__).parent.resolve())
#     path_dir = path_dir[0:-6]
#     path_consts = path_dir + '/constants/'
#     path_const_input = path_consts + 'Teste BEN Input/'
#     path_const_output = path_consts + 'Teste BEN Output/'
#     file = 'BEN.xlsx'
#     ben = BenHandler(file, path_const_input, path_const_output)
#     assert ben.generateTable()


def teste_getTablesNaoExiste():
    """
    Testa se o código detecta quando se passa o caminho até um tabela que não existe

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_output = path_consts + 'Teste BEN Output/'
    file = 'BEN.xlsx'
    ben = BenHandler(file, "scripts/nao_existe.csv", path_const_output)
    assert not ben.generateTable()
