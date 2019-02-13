from flask import Flask, request
from flask_cors import CORS
import json
import Service
import Dao
import _thread


app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/status")
def status():
    module = request.args.get('module')
    if module:
        re = Service.lmstatByModule(module)
    else:
        re = Service.lmstatAll()
    return json.dumps(re)

@app.route("/matlab")
def get_matlab():
    date = request.args.get('date')
    res = Dao.Matlab.objects(date=date)
    return res.to_json()

@app.route("/audio_system_toolbox")
def get_audio_system_toolbox():
    date = request.args.get('date')
    res = Dao.AudioSystemToolbox.objects(date=date)
    return res.to_json()

@app.route("/bioinformatics_toolbox")
def get_bioinformatics_toolbox():
    date = request.args.get('date')
    res = Dao.BioinformaticsToolbox.objects(date=date)
    return res.to_json()

@app.route("/video_and_image_blockset")
def get_video_and_image_blockset():
    date = request.args.get('date')
    res = Dao.VideoandImageBlockset.objects(date=date)
    return res.to_json()

@app.route("/curve_fitting_toolbox")
def get_curve_fitting_toolbox():
    date = request.args.get('date')
    res = Dao.CurveFittingToolbox.objects(date=date)
    return res.to_json()

@app.route("/neural_network_toolbox")
def get_neural_network_toolbox():
    date = request.args.get('date')
    res = Dao.NeuralNetworkToolbox.objects(date=date)
    return res.to_json()

@app.route("/gads_toolbox")
def get_gads_toolbox():
    date = request.args.get('date')
    res = Dao.GadsToolbox.objects(date=date)
    return res.to_json()

@app.route("/map_toolbox")
def get_map_toolbox():
    date = request.args.get('date')
    res = Dao.MapToolbox.objects(date=date)
    return res.to_json()

@app.route("/optimization_toolbox")
def get_optimization_toolbox():
    date = request.args.get('date')
    res = Dao.OptimizationToolbox.objects(date=date)
    return res.to_json()

@app.route("/rf_toolbox")
def get_rf_toolbox():
    date = request.args.get('date')
    res = Dao.RfToolbox.objects(date=date)
    return res.to_json()

if __name__=="__main__":
    _thread.start_new_thread(Service.thread_to_save_data, ())
    app.run()