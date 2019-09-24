from flask import Flask, request
from flask_cors import CORS
import json
import subService
import subDao
import _thread
import Util

app = Flask(__name__)
CORS(app, supports_credentials=True)

lic_file_content = lambda domain, port: ("SERVER " + domain \
    + " 000C292A71EF " + port \
    + " \nDAEMON MLM \"C:\\Program Files\\MATLAB\\R2018b\\etc\\win64\\mlm.exe\" port=27001")

@app.route("/server", methods=['POST'])
def init_server():
    domain = request.json["domain"]
    flex_port = str(request.json["flex_port"])
    web_port = str(request.json["web_port"])
    server = subDao.Server(domain=domain,
						flex_port=flex_port,
						software=request.json["software"],
                        lmstat_lic=request.json["lmstat_lic"],
                        lmgrd_lic=request.json["lmgrd_lic"])
    server.save()

    lic_file = open(request.json["lmstat_lic"], "w")
    lic_file.write(lic_file_content(domain, flex_port))
    lic_file.close()

@app.route("/start", methods=['GET'])
def restart():
    sid = Util.get_sid()
    subService.start(sid)
    return json.dumps(0)

@app.route("/restart", methods=['GET'])
def restart():
    sid = Util.get_sid()
    subService.restart(sid)
    return json.dumps(0)

@app.route("/shutdown", methods=['GET'])
def shutdown():
    sid = Util.get_sid()
    subService.shutdown(sid)
    return json.dumps(0)

@app.route("/realtime", methods=['GET'])
def realtime_data_v2():
    sid = Util.get_sid()
    module = request.args.get('module')
    if module:
        re = subService.lmstatByModule(sid, module)
    else:
        re = subService.lmstatAll(sid)
    return json.dumps(re)

@app.route("/history", methods=['GET'])
def history_data_v2():
    server_id = Util.get_sid()
    software = request.args.get('software', type = str)
    module = request.args.get('module', type = str)
    date = request.args.get('date', type = str)
    res = subDao.History.objects(
        server_id=server_id,
        software=software,
        module=module,
        date=date
    )
    return res.to_json()

if __name__=="__main__":
    _thread.start_new_thread(subService.thread_to_check_server_status, ())
    _thread.start_new_thread(subService.thread_to_save_data, ())
    app.run()