import os
from Command import Command
import Util
import json
import Dao
import time
import requests

minute_interval = 60
cmd = Command()

#testdata = Util.testdata()

status_dic = {}

def lmstatAll(sid):
	server = Dao.Server.objects(id= sid)[0]
	lic_file = server.lmstat_lic
	software = server.software

	status, res = cmd.lmstatAll(lic_file, software)
	status_dic[sid] = status
	return res

def lmstatByModule(sid, module):
	server = Dao.Server.objects(id= sid)[0]
	lic_file = server.lmstat_lic
	software = server.software

	status, res = cmd.lmstatByModule(lic_file, module, software)
	status_dic[sid] = status
	return res

def start(sid):
	res = requests.get(getPath(sid)+"/start").json()
	return res

def shutdown(sid):
	res = requests.get(getPath(sid)+"/shutdown").json()
	return res

def restart(sid):
	res = requests.get(getPath(sid)+"/restart").json()
	return res

def init_server(domain, flex_port, web_port, software, lmstat_lic, lmgrd_lic):
	path = "http://" + domain + ":" + web_port
	payload = {"domain":domain, "flex_port":flex_port,"software":software,"lmstat_lic":lmstat_lic,"lmgrd_lic":lmgrd_lic}
	res = requests.post(path+"/server", params=payload).json()
	return res

def getHistory(server_id, software, module, date):
	payload = {"software":software,"module":module,"date":date}
	res = requests.get(getPath(server_id)+"/history", params=payload).json()
	return res

def getRealtime(sid, module=None):
	payload = {"sid":sid, "module":module}
	res = requests.get(getPath(sid)+"/realtime", params=payload).json()
	return res

def thread_to_check_server_status():
	while(True):
		servers = Dao.Server.objects()
		for server in servers:
			status = cmd.check(server.lmstat_lic)
			status_dic[server.id] = status
			if(status==-1):
				restart(server.id)
			# restart the server once status was wrong
		time.sleep(minute_interval*15)

def getPath(sid):
	server = Dao.Server.objects(id= sid)[0]
	path = "http://" + server.domain +":"+ server.web_port
	return path

def get_status_by_id(sid):
	return status_dic.get(sid)

def _main():
    print(cmd.lmstatAll())

if __name__=="__main__":
    _main()