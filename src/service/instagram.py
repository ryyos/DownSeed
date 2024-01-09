import requests

from uuid import uuid4
from urllib import request
from bs4 import BeautifulSoup
from src.utils.logs import logger

class Instagram:
    def __init__(self) -> None:
        self.__api = 'https://v3.igdownloader.app/api/ajaxSearch'
        self.__headers = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}


    def __curl(self, path: str, url: str):
        try:
            if url: request.urlretrieve(url, path)
        except Exception as err:
            logger.error(err)


    def ex(self, path: str,  post_url: str):

        payload = {'q': post_url, 't' : 'media', 'lang':'id'}
        response = requests.post(url=self.__api, data=payload, headers=self.__headers)
        
        html = BeautifulSoup(response.json()['data'], 'html.parser')

        logger.info(f'content found: {len(html.find_all("div", class_="download-items__btn"))}')
        print()

        for url in html.find_all("div", class_="download-items__btn"):
             
            if 'video' in url.text: self.__curl(path=f'{path}/{uuid4()}.mp4', url=url.a['href'])
            if 'Gambar' in url.text: self.__curl(path=f'{path}/{uuid4()}.jpg', url=url.a['href'])
            
            logger.info('content downloaded successfully')


if __name__ == '__main__':
    ig = Instagram()
    ig.ex(post_url='https://www.instagram.com/p/C1oEJJ-hBqM/?img_index=1', path='')

