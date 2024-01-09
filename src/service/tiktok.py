import requests

from uuid import uuid4
from urllib import request
from bs4 import BeautifulSoup

from src.utils.logs import logger

class Tiktok:
    def __init__(self) -> None:
        self.__api = 'https://ssstik.io/abc?url=dl'
        self.__headers = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}


    def __curl(self, path: str, url: str):
        try:
            if url: request.urlretrieve(url, path)
        except Exception as err:
            logger.error(err)


    def ex(self, path: str, tiktok_url: str):

        payload = {'id': tiktok_url, 'locale' : 'id', 'tt':'RjU5bWlk'}
        response = requests.post(url=self.__api, data=payload, headers=self.__headers)

        print(BeautifulSoup(response.text, 'html.parser').find('a')['href'])
        self.__curl(path=f'{path}/{uuid4()}.mp4', url=BeautifulSoup(response.text, 'html.parser').find('a')['href'])
        logger.info('content downloaded successfully')
