from flask import Flask
from flask_cors import CORS
import json
from Service import cmd_status

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/status")
def status():
    re = cmd_status()
    return json.dumps(re)


if __name__=="__main__":
    app.run()