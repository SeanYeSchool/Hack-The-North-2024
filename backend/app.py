from flask import Flask, request
from flask_cors import CORS
import json
import pandas as pd
from identify import get_angle_diff, get_prediction, read_coords
from model import pose_rec_model
import torch
from variables import pose_map
import logging

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

global model
global currentPose
model = pose_rec_model(3, 128, 32, 5, 16, 8, 0.2)
model.load_state_dict(torch.load("test_model_80.pt", weights_only=False)) 

currentPose = None

@app.route("/setPoseIndex/<string:routine_json>", methods=['GET'])
def setRoutine(routine_json):
    global currentPose
    routine_list = json.loads(routine_json)
    currentPose = routine_list[0]

@app.route("/verifyPose/<string:vectors_json>", methods=['GET'])
def verifyPose(vectors_json):
    '''
    [
        [x, y, z, v] list of list of floats
    ]
    '''
    global currentPose
    vectors_list = json.loads(vectors_json)
    rows = []
    for vector in vectors_list:
        rows.append([vector['x'], vector['y'], vector['z'], vector['visibility']])   
    rows = pd.DataFrame(rows)
    coords = read_coords(rows)
    try:
        prediction = get_prediction(coords, model)
        return str(prediction==currentPose).lower()
    except:
        return False

@app.route("/getComment/<string:comment>")
def getComment(comment):
    #TODO: put voiceflow api thingy
    return f"Post {comment}"

if __name__ == "__main__":
    app.run(debug=True, port=5000)