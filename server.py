from flask import Flask, request
from flask_cors import CORS
import json
import Service
import Dao
import _thread

lic_file_content = lambda domain, port: ("SERVER " + domain \
    + " 000C292A71EF " + port \
    + " \nDAEMON MLM \"C:\\Program Files\\MATLAB\\R2018b\\etc\\win64\\mlm.exe\" port=27001")

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/realtime/<sid>", methods=['GET'])
def realtime_data(sid):
    module = request.args.get('module')
    if module:
        re = Service.lmstatByModule(sid, module)
    else:
        re = Service.lmstatAll(sid)
    return json.dumps(re)

@app.route("/server", methods=['POST'])
def create_server():
    server = Dao.Server(domain=request.json["domain"],\
						port=request.json["port"],\
						software=request.json["software"],\
                        lic=request.json["lic"])
    server.save()

    lic_file = open(request.json["lic"], "w")
    lic_file.write(lic_file_content(request.json["domain"], request.json["port"]))
    lic_file.close()

    return server.to_json()

@app.route("/server/<sid>", methods=['GET'])
def get_server_by_id(sid):
    servers = Dao.Server.objects(id=sid)
    if len(servers) == 0:
        return json.dumps(None)
    server = servers[0]
    return server.to_json()

@app.route("/server/<sid>", methods=['DELETE'])
def delete_server(sid):
    server = Dao.Server.objects(id=sid)
    server[0].delete()
    return None

@app.route("/server", methods=['GET'])
def get_servers():
    res = Dao.Server.objects()
    return res.to_json()

@app.route("/history", methods=['GET'])
def history_data(module):
    server_id = request.args.get('server_id', type = int)
    software = request.args.get('software', type = str)
    module = request.args.get('module', type = str)
    date = request.args.get('date', type = str)
    res = Dao.History.objects(
        server_id=server_id,
        software=software,
        module=module,
        date=date
    )
    return res.to_json()

if __name__=="__main__":
    _thread.start_new_thread(Service.thread_to_save_data, ())
    #_thread.start_new_thread(Service.thread_to_check_server_status, ())
    app.run()