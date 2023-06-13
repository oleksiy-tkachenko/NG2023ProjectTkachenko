from flask import Flask, Response
from flask import request

import time

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def lol():
    if request.method == "GET":
        resp = Response()
        resp.headers['CPU-usage'] = '0'
        return resp
    else:
        resp = Response()
        resp.headers['CPU-usage'] = request.headers['CPU-usage']
        resp.headers['RAM-usage'] = request.headers['RAM-usage']
        return f"{resp.headers['RAM-usage']}, {resp.headers['CPU-usage']}, {request.environ['REMOTE_ADDR']}"

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8081);
    