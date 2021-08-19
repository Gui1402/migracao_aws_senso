import zipfile
import requests
from io import BytesIO
import os
from glob import glob
from shutil import copyfile
import shutil


def download_data() -> None:

    os.makedirs('./censo', exist_ok=True) ## if exists just pass
    url = 'https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_2020.zip'

    ## do download content
    print('\nDownloading files ...')
    file_bytes = BytesIO(requests.get(url).content)
    myzip = zipfile.ZipFile(file_bytes) ## python understand file as zip
    myzip.extractall('./censo')
    print('\nDone')


def move_data(dst_base: str) -> None:
    data_dir = 'censo/microdados_educacao_basica_2020/DADOS/'
    csv_files = glob(f'{data_dir}/*.CSV')
    for f in csv_files:
        fname = f.split('/')[-1]
        dst = f'{dst_base}{fname}'
        print(f'\nCopy file from {f} to {dst}')
        copyfile(f, dst)
        print('\nDONE')

    
def delete_files() -> None:
    print('\nRemoving files')
    shutil.rmtree('./censo', ignore_errors=True)


if __name__=="__main__":
    download_data()
    move_data('../data/')
    delete_files()