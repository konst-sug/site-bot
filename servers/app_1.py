import logging
import schedule
import time
import threading
from flask import Flask, render_template

# Настраиваем логгер
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- 1. Создаем Flask-приложение ---
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("page.html")


# --- 2. Определяем задачу (твоя функция) ---
# Подразумевается, что test_thread() из test_run.py уже готов к работе.
from test_run import test_thread 

def job_wrapper():
    """Эта функция будет вызываться планировщиком."""
    try:
        # Вызываем твою основную логику
        test_thread()
        logger.info("Фоновая задача выполнена успешно.")
    except Exception as e:
        logger.error(f"Ошибка в фоновой задаче: {e}")


# --- 3. Функция для запуска планировщика в фоне ---
def run_scheduler():
    # Говорим планировщику: "запускай job_wrapper() каждые 3 часа"
    schedule.every(3).hours.do(job_wrapper)
    logger.info("Фоновый планировщик запущен.")

    # Бесконечный цикл, который проверяет, не пора ли запустить задачу
    while True:
        schedule.run_pending()
        time.sleep(1) # Ждем 1 секунду перед следующей проверкой


# --- 4. Запускаем всё ---
if __name__ == '__main__':
    # --- ЭТО ГЛАВНАЯ ЧАСТЬ ---
    # Создаем отдельный поток (thread) для планировщика.
    # Он будет работать в фоне (демоном).
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()

    # --- Запускаем ТОЛЬКО веб-сервер ---
    # Веб-сервер не знает и не заботится о планировщике.
    # Он просто ждёт HTTP-запросы на порту 8888.
    app.run(host='0.0.0.0', port=8888)