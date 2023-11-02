import pathlib
from ..handlers.anuarioANPHandler import AnuarioANPHandler
from ..scrappers.excelScrapperAnuarioANP import ExcelScrapperAnuarioANP


def teste_getTabelasGN_caminhoErrado():
    """
    Testa se o código detecta um erro caso tenha sido fornecido um caminho errado para o repositório do arquivo de origem

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Errado/'
    path_const_output = path_consts + 'Teste Anuario ANP Output/'
    handler = AnuarioANPHandler(path_const_input, path_const_output)
    dic_tab_nomes = {
        "tabela1-6.csv": ["ResProvGNPaises.csv", 2, "val_res"],
        "tabela1-7.csv": ["ProdGNPaises.csv", 2, "val_prod"],
        "tabela1-8.csv": ["ConsGNPaises.csv", 1, "val_cons"]
    }
    assert not handler.generateTablesGN(dic_tab_nomes)


def teste_getTabelasPetGNNac_caminhoErrado():
    """
    Testa se o código detecta um erro caso tenha sido fornecido um caminho errado para o repositório do arquivo de origem

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Errado/'
    path_const_output = path_consts + 'Teste Anuario ANP Output/'
    handler = AnuarioANPHandler(path_const_input, path_const_output)
    dic_tab_nomes = {
        "tabela2-9.csv": ["ProdPetrUF.csv", "prod_pet"],
        "tabela2-13.csv": ["ProdGNUF.csv", "prod_gn"],
        "tabela2-16.csv": ["QueimaPerdaGNUF.csv", "queima_perda_pet"]
    }
    assert not handler.generateTablesPetGNNac(dic_tab_nomes)


def teste_getTabelasBioCombs_caminhoErrado():
    """
    Testa se o código detecta um erro caso tenha sido fornecido um caminho errado para o repositório do arquivo de origem

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Errado/'
    path_const_output = path_consts + 'Teste Anuario ANP Output/'
    handler = AnuarioANPHandler(path_const_input, path_const_output)
    dic_tab_nomes = {
        "tabela4-1.csv": ["ProdEtAniHidUF.csv", "prod_etanol_anidro_hidr"],
        "tabela4-10.csv": ["ProdB100UF.csv", "prod_biodiesel"]
    }
    assert not handler.generateTablesBioCombs(dic_tab_nomes)


def teste_getTabelasCBIO_caminhoErrado():
    """
    Testa se o código detecta um erro caso tenha sido fornecido um caminho errado para o repositório do arquivo de origem

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Errado/'
    path_const_output = path_consts + 'Teste Anuario ANP Output/'
    handler = AnuarioANPHandler(path_const_input, path_const_output)
    dic_tab_nomes = {
        "tabela4-16.csv": ["EmCBIOBioComb.csv", "biocombustivel", "emissao_cbio"],
        "tabela4-17.csv": ["ApCBIO.csv", "distribuidores_combustivel", "outros_agentes"]
    }
    assert not handler.generateTablesCBIO(dic_tab_nomes, 2022)


def teste_getAnuarioANP_linkErrado():
    """
    Testa se o código detecta caso insira o link errado para encontrar o arquivo

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_raiz = path_dir[0:-7]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Input/'
    url_site = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/anuario-"
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
    scrapper = ExcelScrapperAnuarioANP(url_site + "2023", path_raiz, path_const_input)
    assert not scrapper.getFiles(tab_nomes)


def teste_getAnuarioANP():
    """
    Testa se o código baixa os arquivos desejados

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_raiz = path_dir[0:-7]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Input/'
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
    scrapper = ExcelScrapperAnuarioANP(url_site + "2023", path_raiz, path_const_input)
    assert scrapper.getFiles(tab_nomes)


def teste_getLinks():
    """
    Testa se o conjunto de links não é vazio

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_raiz = path_dir[0:-7]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Input/'
    url_site = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/anuario-estatistico-"
    scrapper = ExcelScrapperAnuarioANP(url_site + "2023", path_raiz, path_const_input)
    assert len(scrapper.getLinks())


def teste_getTabelasGN():
    """
    Testa se o código pega as tabelas de Gás Natural

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Input/'
    path_const_output = path_consts + 'Teste Anuario ANP Output/'
    handler = AnuarioANPHandler(path_const_input, path_const_output)
    dic_tab_nomes = {
        "tabela1-6.csv": ["ResProvGNPaises.csv", 2, "val_res"],
        "tabela1-7.csv": ["ProdGNPaises.csv", 2, "val_prod"],
        "tabela1-8.csv": ["ConsGNPaises.csv", 1, "val_cons"]
    }
    assert handler.generateTablesGN(dic_tab_nomes)


def teste_getTabelasPetGNNac():
    """
    Testa se o código pega as tabelas de Petróleo e Gás Natural nacionalmente

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Input/'
    path_const_output = path_consts + 'Teste Anuario ANP Output/'
    handler = AnuarioANPHandler(path_const_input, path_const_output)
    dic_tab_nomes = {
        "tabela2-9.csv": ["ProdPetrUF.csv", "prod_pet"],
        "tabela2-13.csv": ["ProdGNUF.csv", "prod_gn"],
        "tabela2-16.csv": ["QueimaPerdaGNUF.csv", "queima_perda_pet"]
    }
    assert handler.generateTablesPetGNNac(dic_tab_nomes)


def teste_getTabelasBioCombs():
    """
    Testa se o código pega as tabelas de Biocombustíveis

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Input/'
    path_const_output = path_consts + 'Teste Anuario ANP Output/'
    handler = AnuarioANPHandler(path_const_input, path_const_output)
    dic_tab_nomes = {
        "tabela4-1.csv": ["ProdEtAniHidUF.csv", "prod_etanol_anidro_hidr"],
        "tabela4-10.csv": ["ProdB100UF.csv", "prod_biodiesel"]
    }
    assert handler.generateTablesBioCombs(dic_tab_nomes)


def teste_getTabelasCBIO():
    """
    Testa se o código pega as tabelas de CBIO

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario ANP Input/'
    path_const_output = path_consts + 'Teste Anuario ANP Output/'
    handler = AnuarioANPHandler(path_const_input, path_const_output)
    dic_tab_nomes = {
        "tabela4-16.csv": ["EmCBIOBioComb.csv", "biocombustivel", "emissao_cbio"],
        "tabela4-17.csv": ["ApCBIO.csv", "distribuidores_combustivel", "outros_agentes"]
    }
    assert handler.generateTablesCBIO(dic_tab_nomes, 2022)
