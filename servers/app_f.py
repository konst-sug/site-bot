from logging import getLogger
from flask import Flask, render_template
from flask_apscheduler import APScheduler

from test_run import test_thread 

logger = getLogger(__name__)
app = Flask(__name__)

# 1. Настраиваем конфиг для планировщика (если нужно)
app.config['SCHEDULER_API_ENABLED'] = False 

# 2. Создаем экземпляр планировщика.
#    На этом этапе НЕ инициализируем его через app.
scheduler = APScheduler()

@app.route("/")
def index():
    return render_template("page.html")


# 3. Определяем задачу.
def cron_job_function():
    """Синхронная задача для планировщика."""
    try:
        test_thread() 
        logger.info("Cron job executed successfully")
    except Exception as e:
        logger.error(f"Cron job failed: {e}")


# Используем "Фабрику приложений" или просто логику запуска.
# Инициализируем планировщик ПЕРЕД запуском приложения/сервера
scheduler.init_app(app)

# Добавляем задачу через API планировщика, а не через декоратор
scheduler.add_job(
    id='main_cron_job',
    func=cron_job_function, # Передаем саму функцию, БЕЗ вызова ()
    trigger='interval',
    hours=3,
    max_instances=1
)

# Запускаем планировщик
scheduler.start()
print("Переход к рабочему потоку...")

# Эта переменная нужна для Gunicorn (wsgi:app)
# Без неё Gunicorn не будет знать, что запускать.
application = app