import os
import click

from dotenv import *
from src import Instagram
from src import Tiktok
from src import write

class Main:

    @click.group()
    @staticmethod
    def sosmed(): ...


    @sosmed.command('update_path')
    @click.option('--path', '-p', help='Enter the path where you want to save')
    def update_path(path: str):
        if not os.path.exists('.env'): write.write_str('.env', '')

        file = find_dotenv()

        set_key(file, 'PATH', path)
        os.getenv('PATH')
        ...

    @sosmed.command('instagram')
    @click.option('--url', '-u', help='insert url contents')
    def instagram(url: str):
        instagram = Instagram()

        load_dotenv()

        PATH = os.getenv('PATH')
        instagram.ex(path=PATH, post_url=url)
        ...

    @sosmed.command('tiktok')
    @click.option('--url', '-u', help='insert your contents')
    def tiktok(self, url: str):
        tiktok = Tiktok()

        load_dotenv()

        PATH = os.getenv('PATH')
        tiktok.ex(path=PATH, tiktok_url=url)
        ...

if __name__ == '__main__':
    main = Main()
    main.sosmed()
    



    


