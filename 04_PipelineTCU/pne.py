import requests
import zipfile
import os
from io import BytesIO

# Deve encontrar os arquivos de entrada disponibilizados no site da EPE
if __name__ == '__main__':
    diretorio = "./constants/Dados_saida_eletricidade"
    os.makedirs(diretorio, exist_ok=True)
    url = "https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-227/topico-563/Dados_saida_eletricidade.zip" 
    filebytes = BytesIO(
        requests.get(url).content
    )
    zip = zipfile.ZipFile(filebytes)
    zip.extractall(diretorio)