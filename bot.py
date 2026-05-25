# bott.py
import requests
from log_config import logger

from sys import exit
from config import choice, url
from funcs import *


def is_url_reachable(url):
    #---Проверка доступности страницы ---
    try:
        response = requests.head(url)  # или requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def main():
    auth_res = False
    if is_url_reachable(url):
        session_block = choice(list(data.keys()))
        try:
            logger.info("Переход к рабочему потоку...")
            func = f"start_{session_block}"
            session_data = choice(data[session_block])
            logger.info(session_data)
            res = globals()[func](*session_data)
        
        except Exception as err:
            logger.error("Ошибка:", str(err))
    else:
        logger.info("Работа прервана из-за ошибки авторизации.")
        exit(1)


if __name__ == '__main__':
    main()