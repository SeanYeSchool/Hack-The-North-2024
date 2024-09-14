from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/setVectors/<string:vectors_json>", methods='POST')
def setVector(vectors_json):
    '''
    [
        [x, y, z, v] list of list of floats
    ]
    '''
    vectors_list = request.get_json()
    # vectors_list = json.loads(vectors_json)
    with open("vectors.txt", "w") as f:
        accumulator = ""
        for vector in vectors_list:
            accumulator += f"{vector[0]} {vector[1]} {vector[2]} {vector[3]}\n"

        accumulator = accumulator.strip("\n")
        f.write(accumulator)

    return f"Post {accumulator}"

@app.route("/getComment/<string:comment>")
def getComment(comment):
    #TODO: put voiceflow api thingy
    return f"Post {comment}"
