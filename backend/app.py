from flask import Flask, request
from flask_cors import CORS
import json
import pandas as pd
from identify import get_angle_diff, get_prediction, read_coords
from model import pose_rec_model
import torch

app = Flask(__name__)
CORS(app)

model = None

def load_model():
    global model
    model = pose_rec_model(3, 128, 32, 5, 16, 8, 0.2)
    model.load_state_dict(torch.load("backend/test_model_80.pt", weights_only=False)) 

@app.before_first_request
def initialize():
    load_model()

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
    df = pd.concat(rows)
    coords = read_coords(df)
    prediction = get_prediction(coords, model)
    angle_diff = get_angle_diff(prediction, coords)
    return prediction, angle_diff

@app.route("/getComment/<string:comment>")
def getComment(comment):
    #TODO: put voiceflow api thingy
    return f"Post {comment}"
