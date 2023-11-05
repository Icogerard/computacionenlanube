# La imagen de Docker contiene el siguiente código
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showResponse():
    html = "<div style='text-align:center;margin:20px;'><h1>Saludos desde México!</h1><img src='https://storage.cloud.google.com/wcs_bucket_01/wcs/images/watbot.png' width='40%' alt='Response @ WCS'></div>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
