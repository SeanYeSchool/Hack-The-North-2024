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
model = pose_rec_model(3, 128, 32, 5, 16, 8, 0.2)
model.load_state_dict(torch.load("test_model_80.pt", weights_only=False)) 
routineIds = None

@app.route("/setRoutine/<string:routine_json>", methods=['GET'])
def setRoutine(routine_json):
    global routineIds
    routine_list = json.loads(routine_json)
    routineIds = []
    for routine in routine_list:
        routineIds.append(pose_map[routine])
    return True

@app.route("/setVectors/<string:vectors_json>", methods=['GET'])
def setVector(vectors_json):
    '''
    [
        [x, y, z, v] list of list of floats
    ]
    '''
    vectors_list = json.loads(vectors_json)
    rows = []
    for vector in vectors_list:
        rows.append([vector['x'], vector['y'], vector['z'], vector['visibility']])   
    rows = pd.DataFrame(rows)
    coords = read_coords(rows)
    prediction = get_prediction(coords, model)
    angle_diff = get_angle_diff(prediction, coords)
    return str(prediction)

@app.route("/getComment/<string:comment>")
def getComment(comment):
    #TODO: put voiceflow api thingy
    return f"Post {comment}"

if __name__ == "__main__":
    app.run(debug=True, port=5000)