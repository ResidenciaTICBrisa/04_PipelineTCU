import requests
import pathlib

if __name__ == '__main__':
    url_epe = "https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-160/topico-168/Anuário Estatístico de Energia Elétrica 2023 - Workbook.xlsx"
    arquivo = "Anuario.xlsx" 
    r = requests.get(url_epe, allow_redirects=True)
    output = open(arquivo, 'wb')
    output.write(r.content)
    output.close()
    path = str(pathlib.Path(__file__).parent.resolve()) 
    pathlib.Path(path + '/' + arquivo).rename(path + '/constants/' + arquivo)