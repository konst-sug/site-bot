from bottle import Bottle, run
from cron_run import start_scheduler

app = Bottle()

start_scheduler()

@app.get("/")
def index():
    return "OK"

run(app, host="0.0.0.0", port=8080)