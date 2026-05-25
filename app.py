from flask import Flask
from cron_run import start_scheduler

app = Flask(__name__)

start_scheduler()


@app.route("/")
def index():
    return "OK"