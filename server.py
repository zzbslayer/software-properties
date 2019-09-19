from flask import Flask, request
from flask_cors import CORS
import json
import Service
import Dao
import os
import _thread

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/server", methods=['GET'])
def get_servers():
    res = Dao.Server.objects()
    return res.to_json()

@app.route("/server/<sid>", methods=['GET'])
def get_server_by_id(sid):
    servers = Dao.Server.objects(id=sid)
    if len(servers) == 0:
        return json.dumps(None)
    server = servers[0]
    return server.to_json()

@app.route("/server", methods=['POST'])
def create_server():
    domain = request.json["domain"]
    flex_port = str(request.json["flex_port"])
    web_port = str(request.json["web_port"])
    server = Dao.Server(domain=domain,
						web_port=web_port,
						software=request.json["software"])
    server.save()
    Service.init_server(domain, flex_port, web_port, request.json["software"], request.json["lmstat_lic"], request.json["lmgrd_lic"])
    return server.to_json()

@app.route("/server/<sid>", methods=['DELETE'])
def delete_server(sid):
    server = Dao.Server.objects(id=sid)
    server[0].delete()
    return None

@app.route("/history", methods=['GET'])
def history_data():
    server_id = request.args.get('server_id', type = str)
    software = request.args.get('software', type = str)
    module = request.args.get('module', type = str)
    date = request.args.get('date', type = str)
    res = Service.getHistory(server_id, software, module, date)
    return res.to_json()

@app.route("/realtime", methods=['GET'])
def realtime_data():
    sid = request.args.get('server_id', type=str)
    module = request.args.get('module', type=str)
    if module:
        re = Service.getRealtime(sid, module)
    else:
        re = Service.getRealtime(sid)
    return json.dumps(re)

@app.route("/start", methods=['GET'])
def restart():
    sid = request.args.get('server_id', type=str)
    Service.start(sid)
    return json.dumps(0)

@app.route("/restart", methods=['GET'])
def restart():
    sid = request.args.get('server_id', type=str)
    Service.restart(sid)
    return json.dumps(0)

@app.route("/shutdown", methods=['GET'])
def shutdown():
    sid = request.args.get('server_id', type=str)
    Service.shutdown(sid)
    return json.dumps(0)

if __name__=="__main__":
    app.run()