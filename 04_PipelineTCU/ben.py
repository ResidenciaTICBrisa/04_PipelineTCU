import requests
import pathlib

if __name__ == '__main__':
    url = "https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-748/topico-678/Anexo IX - Balanços Energéticos Consolidados (em tep) 1970 - 2022.xlsx"
    arquivo = "BEN.xlsx" 
    r = requests.get(url, allow_redirects=True)
    output = open(arquivo, 'wb')
    output.write(r.content)
    output.close()
    path = str(pathlib.Path(__file__).parent.resolve()) 
    pathlib.Path(path + '/' + arquivo).rename(path + '/constants/' + arquivo)