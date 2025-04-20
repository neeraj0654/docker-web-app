from flask import Flask, render_template
import psutil
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime_str = str(uptime).split('.')[0]

    return render_template(
        "index.html",
        cpu=cpu,
        memory=memory,
        disk=disk,
        uptime=uptime_str
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
