import os
from Command import Command
import Util
import json
import Dao
import time

modules = Util.modules()

minute_interval = 1
cmd = Command()

#testdata = Util.testdata()

def all_status():
    return cmd.all_status()

def thread_to_save_data():
    while(True):
        now_time = Util.get_time()
        now_date = Util.get_date()
        #data = Util.testdata()
        data = cmd_status()

        matlab_data = data["MATLAB"] 
        matlab = Dao.Matlab(date=now_date,time=now_time,\
                        total=matlab_data["total"],\
                        use=matlab_data["use"],\
                        metadata=matlab_data["metadata"],\
                        user_data=matlab_data["user_data"]\
                        )
        matlab.save()

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
        gt = Dao.GadsToolbox(date=now_date,time=now_time,\
                        total=gt_data["total"],\
                        use=gt_data["use"],\
                        metadata=gt_data["metadata"],\
                        user_data=gt_data["user_data"]\
                        )
        gt.save()

        mt_data = data["MAP_Toolbox"]
        mt = Dao.MapToolbox(date=now_date,time=now_time,\
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
        rt = Dao.RfToolbox(date=now_date,time=now_time,\
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
        print("Save Completed.")

        time.sleep(minute_interval*60)

def _main():
    print(cmd_status())

if __name__=="__main__":
    _main()