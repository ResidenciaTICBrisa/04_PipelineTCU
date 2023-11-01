import requests
import re
from bs4 import BeautifulSoup
from pathlib import Path


class ExcelScrapperIEA:
    def __init__(self, url, path_raiz):
        self.url = url
        self.nome_arquivo = None
        self.path_raiz = path_raiz

        self.download_link = None
        self.diretorio = '/constants/IEA/'
        self.path_destino = None
    def baixa_arquivo(self) -> bool:
        response = requests.get(self.url)
        # Verifica se a requisição foi bem-sucedida (código 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            download_button = soup.find('a', attrs={'download': True, 'href': True})
            self.download_link = download_button['href']
            print(self.download_link)
            self.nome_arquivo = re.search(r'[^/]+$', self.download_link).group(0)
            print(self.nome_arquivo)

        if self.download_link:
            download_response = requests.get(self.download_link)
            if download_response.status_code == 200:
                self.path_destino = Path(self.path_raiz + self.diretorio + self.nome_arquivo)
                self.path_destino.parent.mkdir(parents=True, exist_ok=True)
                with open(str(self.path_destino), 'wb') as file:
                    file.write(download_response.content)
            return True
        else:
            return False
