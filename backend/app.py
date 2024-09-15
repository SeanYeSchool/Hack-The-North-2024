from flask import Flask, request
from flask_cors import CORS
import json
import pandas as pd
from identify import get_angle_diff, get_prediction, read_coords
from model import pose_rec_model
import torch
from variables import pose_map
import logging
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

global model
global targetPose
model = pose_rec_model(3, 128, 32, 5, 16, 8, 0.2)
model.load_state_dict(torch.load("test_model_80.pt", weights_only=False)) 

targetPose = None

@app.route("/setPoseIndex/<string:pose_json>", methods=['GET'])
def setPoseIndex(pose_json):
    print(pose_json)
    global targetPose
    pose = str(json.loads(pose_json)).lower().replace(' ', '')
    print(pose)
    try:
        targetPose = pose_map[pose]
        return "true"
    except:
        return "false"

@app.route("/verifyPose/<string:vectors_json>", methods=['GET'])
def verifyPose(vectors_json):
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
    try:
        prediction = get_prediction(coords, model)
        print(prediction, targetPose)
        return str(prediction==targetPose).lower()
    except:
        return "error"

#Note angle must be a float not 1 but 1.0 will work
@app.route("/getComment/<float:angle_margin_of_error>/<string:vectors_json>")
def getComment(angle_margin_of_error, vectors_json):
    '''
    Simple mistake criteria cases (we can add more than one later on)

    Downwards Dog: Being Flat

    Goddess: Not spreading legs (knees or feet to close togther)

    Plank: Head, and Feet must be on the line that intersects the torso

    Tree: Feet vertical positions are around the same

    Warrior2: Hands are not straightly spread out
    '''
    global targetPose
    if targetPose == None:
        return "targetPose is None"
    
    #currentPose = 0 #For debugging purposes
    vectors_list = json.loads(vectors_json) #Do math with this to varify test cases
    rows = []
    for vector in vectors_list:
        rows.append([vector['x'], vector['y'], vector['z'], vector['visibility']])   
    rows = pd.DataFrame(rows)
    coords = read_coords(rows)

    angle_diff = get_angle_diff(targetPose, coords) #We assume the current pos is the predicted one
    target_bodypart = None
    for bodypart in angle_diff:
        if angle_diff[bodypart] > angle_margin_of_error:
            target_bodypart = bodypart
    
    api_key = 'VF.DM.66e66fed380effe3d506ded2.Au880xsdyUQw2vsF' # it should look like this: VF.DM.XXXXXXX.XXXXXX... keep this a secret!

    # user_id defines who is having the conversation, e.g. steve, john.doe@gmail.com, username_464
    def interact(request):
        response = requests.post(
            'https://general-runtime.voiceflow.com/state/user/cm134yu9e00eu3j7k2slbmxhi/interact',
            json={ 'request': request },
            headers={ 
                'Authorization': api_key,
                'versionID': 'production'
            },
        )
    
        return response.json()

    interact({'type' : 'launch'}) #Launch VoiceFlow
    if target_bodypart == None:
        response_json = interact({'type' : 'text', 'payload' : 'Say an encouraging message relating to great work'})
    else:
        message = "A person is doing the "
        message += tuple(pose_map.keys())[targetPose]
        message += " but their " 
        message += target_bodypart
        message += " is at an incorrect angle. What feedback can you give for the person to improve?"
        response_json = interact({'type' : 'text', 'payload' : message})
    
    if response_json:
        return f"GET{response_json[1]['payload']['message']}"
    else:
        return "Keep it up!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)