import logging
import schedule
import time
import threading
from flask import Flask, render_template

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("page.html")


from test_run import test_thread 

def job_wrapper():
    """Эта функция будет вызываться планировщиком."""
    try:
        # Вызываем основную логику
        test_thread()
        logger.info("Фоновая задача выполнена успешно.")
    except Exception as e:
        logger.error(f"Ошибка в фоновой задаче: {e}")


#  Функция для запуска планировщика в фоне ---
def run_scheduler():
    # "запускай job_wrapper() каждые 3 часа"
    schedule.every(3).hours.do(job_wrapper)
    logger.info("Фоновый планировщик запущен.")

    # Бесконечный цикл, который проверяет, не пора ли запустить задачу
    while True:
        schedule.run_pending()
        time.sleep(10) # Ждем перед следующей проверкой


#  Запускаем всё ---
if __name__ == '__main__':
    # Создаем отдельный поток (thread) для планировщика.
    # Он будет работать в фоне (демоном).
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()

    # Он просто ждёт HTTP-запросы на порту 8888.
    app.run(host='0.0.0.0', port=8888)
