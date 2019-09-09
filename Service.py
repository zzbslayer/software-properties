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
	lic_file = server.lic
	software = server.software

	status, res = cmd.lmstatAll(lic_file, software)
	status_dic[sid] = status
	return res

def lmstatByModule(sid, module):
	server = Dao.Server.objects(id= sid)[0]
	lic_file = server.lic
	software = server.software

	status, res = cmd.lmstatByModule(lic_file, module, software)
	status_dic[sid] = status
	return res

def thread_to_check_server_status():
	while(True):
		servers = Dao.Server.objects()
		for server in servers:
			status = cmd.check(server.lic)
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
			print("[Thread.save_data] " + now_date + " " + now_time + " " + server.lic)
			status, data = cmd.lmstatAll(server.lic, server.software)
			status_dic[server.id] = status
			
			if status != 0:
                print("[Thread.save_data] Server status:" + str(status))
				continue

			for module in data:
				record_data = data[module]
                res = Dao.History(server_id = server.id,\
                    software=server.software,\
                    module=module,\
                    date=now_date,time=now_time,\
					total=record_data["total"],\
					use=record_data["use"],\
					metadata=record_data["metadata"],\
					user_data=record_data["user_data"])
				res.save()

			print("[Thread.save_data] " + server.software) 
			#print("[Thread.save_data] " + res.to_json())

		'''
        ast_data = data["Audio_System_Toolbox"]
        ast = Dao.AudioSystemToolbox(date=now_date,time=now_time,\
                        total=ast_data["total"],\
                        use=ast_data["use"],\
                        metadata=ast_data["metadata"],\
                        user_data=ast_data["user_data"]\
                        )
        ast.save()

        bt_data = data["Bioinformatics_Toolbox"]
        bt = Dao.BioinformaticsToolbox(date=now_date,time=now_time,\
                        total=bt_data["total"],\
                        use=bt_data["use"],\
                        metadata=bt_data["metadata"],\
                        user_data=bt_data["user_data"]\
                        )
        bt.save()

        vi_data = data["Video_and_Image_Blockset"]
        vi = Dao.VideoandImageBlockset(date=now_date,time=now_time,\
                        total=vi_data["total"],\
                        use=vi_data["use"],\
                        metadata=vi_data["metadata"],\
                        user_data=vi_data["user_data"]\
                        )
        vi.save()

        cft_data = data["Curve_Fitting_Toolbox"]
        cft = Dao.CurveFittingToolbox(date=now_date,time=now_time,\
                        total=cft_data["total"],\
                        use=cft_data["use"],\
                        metadata=cft_data["metadata"],\
                        user_data=cft_data["user_data"]\
                        )
        cft.save()

        nn_data = data["Neural_Network_Toolbox"]
        nn = Dao.NeuralNetworkToolbox(date=now_date,time=now_time,\
                        total=nn_data["total"],\
                        use=nn_data["use"],\
                        metadata=nn_data["metadata"],\
                        user_data=nn_data["user_data"]\
                        )
        nn.save()

        gt_data = data["GADS_Toolbox"]
        gt = Dao.GADSToolbox(date=now_date,time=now_time,\
                        total=gt_data["total"],\
                        use=gt_data["use"],\
                        metadata=gt_data["metadata"],\
                        user_data=gt_data["user_data"]\
                        )
        gt.save()

        mt_data = data["MAP_Toolbox"]
        mt = Dao.MAPToolbox(date=now_date,time=now_time,\
                        total=mt_data["total"],\
                        use=mt_data["use"],\
                        metadata=mt_data["metadata"],\
                        user_data=mt_data["user_data"]\
                        )
        mt.save()

        ot_data = data["Optimization_Toolbox"]
        ot = Dao.OptimizationToolbox(date=now_date,time=now_time,\
                        total=ot_data["total"],\
                        use=ot_data["use"],\
                        metadata=ot_data["metadata"],\
                        user_data=ot_data["user_data"]\
                        )
        ot.save()

        rt_data = data["RF_Toolbox"]
        rt = Dao.RFToolbox(date=now_date,time=now_time,\
                        total=rt_data["total"],\
                        use=rt_data["use"],\
                        metadata=rt_data["metadata"],\
                        user_data=rt_data["user_data"]\
                        )
        rt.save()

        psb_data = data["Power_System_Blocks"]
        psb = Dao.PowerSystemBlocks(date=now_date,time=now_time,\
                        total=psb_data["total"],\
                        use=psb_data["use"],\
                        metadata=psb_data["metadata"],\
                        user_data=psb_data["user_data"]\
                        )
        psb.save()

        scd_data = data["Simulink_Control_Design"]
        scd = Dao.SimulinkControlDesign(date=now_date,time=now_time,\
                        total=scd_data["total"],\
                        use=scd_data["use"],\
                        metadata=scd_data["metadata"],\
                        user_data=scd_data["user_data"]\
                        )
        scd.save()

        st_data = data["Symbolic_Toolbox"]
        st = Dao.SymbolicToolbox(date=now_date,time=now_time,\
                        total=st_data["total"],\
                        use=st_data["use"],\
                        metadata=st_data["metadata"],\
                        user_data=st_data["user_data"]\
                        )
        st.save()

        wt_data = data["Wavelet_Toolbox"]
        wt = Dao.WaveletToolbox(date=now_date,time=now_time,\
                        total=wt_data["total"],\
                        use=wt_data["use"],\
                        metadata=wt_data["metadata"],\
                        user_data=wt_data["user_data"]\
                        )
        wt.save()
		'''
		now_time = Util.get_time()
		print("[Thead.save_data] End: " + now_time)
		time.sleep(minute_interval*60)

def _main():
    print(cmd.lmstatAll())

if __name__=="__main__":
    _main()