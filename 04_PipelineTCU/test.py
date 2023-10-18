import requests
import re
from bs4 import BeautifulSoup
import ieaHandler as ieaH

url = 'https://www.iea.org/data-and-statistics/data-product/world-energy-statistics-and-balances'
if __name__ == '__main__':
    response = requests.get(url)
    download_link = None
    diretorio = '../constants/IEA'
    # Verifica se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        download_button = soup.find('a', attrs={'download': True, 'href': True})
        download_link = download_button['href']
        nome_do_arquivo = re.sub(r'\([^)]*\)', '', download_button.find('span',class_='m-block__downloadfiles__label').text)
        nome_do_arquivo = re.sub(r'\s+', '_', nome_do_arquivo)
    if download_link:
        download_response = requests.get((download_link))
        if download_response.status_code == 200:
            with open(nome_do_arquivo, 'wb') as file:
                file.write(download_response.content)
            parser = ieaH()