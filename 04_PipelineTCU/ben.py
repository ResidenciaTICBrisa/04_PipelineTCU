import requests
from bs4 import BeautifulSoup
import pathlib

if __name__ == '__main__':
    url = "https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/BEN-Series-Historicas-Completas"
    url_epe = "https://www.epe.gov.br"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'}
    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
    arquivo = "BEN.xlsx" 
    a = soup.select_one('[href*="Matrizes Consolidadas"]')
    link = url_epe + a['href']
    r = requests.get(link, allow_redirects=True)
    output = open(arquivo, 'wb')
    output.write(r.content)
    output.close()
    path = str(pathlib.Path(__file__).parent.resolve()) 
    pathlib.Path(path + '/' + arquivo).rename(path + '/constants/' + arquivo)