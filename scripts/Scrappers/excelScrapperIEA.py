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
        self.diretorio = '/scripts/constants/IEA/'
        self.path_destino = None
    def baixa_arquivo(self) -> str:
        response = requests.get(self.url)
        # Verifica se a requisição foi bem-sucedida (código 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            download_button = soup.find('a', attrs={'download': True, 'href': True})
            self.download_link = download_button['href']
            self.nome_arquivo = re.search(r'[^/]+$', self.download_link).group(0)
        else:
            raise ValueError(f"Não foi possivel acessar a url {self.url} \n")

        if self.download_link:
            download_response = requests.get(self.download_link)
            if download_response.status_code == 200:
                self.path_destino = Path(self.path_raiz + self.diretorio + self.nome_arquivo)
                self.path_destino.parent.mkdir(parents=True, exist_ok=True)
                with open(str(self.path_destino), 'wb') as file:
                    file.write(download_response.content)
                return self.nome_arquivo
            else:
                raise ValueError(f"Não foi possivel baixar o arquivo {self.nome_arquivo} \n")
        else:
            raise ValueError(f"Não existe link para download \n")
