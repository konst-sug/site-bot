# test_run.py
import requests

from log_config import logger
from sys import exit
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from config import url, choice, INTERVAL
from funcs import *

scheduler = BackgroundScheduler()


def is_url_reachable(url):
    #---Проверка доступности страницы ---
    try:
        response = requests.head(url)  # или requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def work_thread():
    if is_url_reachable(url):
        session_block = choice(list(data.keys()))
        logger.info(session_block)
        try:
            logger.info("Redirect to work bot...")
            func = f"start_{session_block}"
            session_data = choice(data[session_block])
            logger.info(session_data)
            res = globals()[func](*session_data)
        
        except Exception as err:
            logger.error("Users actions bot error: %s", str(err))
    else:
        logger.error("Work_thread error: %s", str(err))
        exit(1)


def start_scheduler():
    scheduler.add_job(
        work_thread,
        trigger='interval',
        hours=INTERVAL,
        id='test_thread_job',
        next_run_time=datetime.now()
    )
    scheduler.start()