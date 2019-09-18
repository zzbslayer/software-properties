import os
from Command import Command
import Util
import json
import Dao
import time

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
	server = Dao.Server.objects(id= sid)[0]
	lmgrd_lic = server.lmgrd_lic

	cmd.start(lmgrd_lic)

def shutdown(sid):
	server = Dao.Server.objects(id= sid)[0]
	lmgrd_lic = server.lmgrd_lic

	cmd.shutdown(lmgrd_lic)

def restart(sid):
	server = Dao.Server.objects(id= sid)[0]
	lmgrd_lic = server.lmgrd_lic

	cmd.shutdown(lmgrd_lic)
	cmd.start(lmgrd_lic)

def thread_to_check_server_status():
	while(True):
		servers = Dao.Server.objects()
		for server in servers:
			status = cmd.check(server.lmstat_lic)
			status_dic[server.id] = status

		time.sleep(minute_interval*15)
		
def get_status_by_id(sid):
	return status_dic.get(sid)


def thread_to_save_data():
	while(True):
		now_time = Util.get_time()
		print("[Thread.save_data] Start: " + now_time)
		servers = Dao.Server.objects()
		for server in servers:
			now_time = Util.get_time()
			now_date = Util.get_date()
			print("[Thread.save_data] " + now_date + " " + now_time + " " + server.lmstat_lic)
			status, data = cmd.lmstatAll(server.lmstat_lic, server.software)
			status_dic[server.id] = status
			if status:
				print("[Tread.save_data] Server status:"+str(status))
				continue
			for module in data:
				record_data = data[module]
				res = Dao.History(
					server_id=str(server.id),
					software=server.software,
					module=module,
					date=now_date,time=now_time,
			        total=record_data["total"],
					use=record_data["use"],
					metadata=record_data["metadata"],
					user_data=record_data["user_data"]
					)
				res.save()
			print("[Thread.save_data] " + server.software) 
			#print("[Thread.save_data] " + res.to_json())
		now_time = Util.get_time()
		print("[Thead.save_data] End: " + now_time)
		time.sleep(minute_interval*60)
		print('\n')

def _main():
    print(cmd.lmstatAll())

if __name__=="__main__":
    _main()
