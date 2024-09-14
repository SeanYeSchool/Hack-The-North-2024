from flask import Flask
import json
app = Flask(__name__)

@app.route("/setVectors/<string:vectors_json>")
def getVector(vectors_json):
    '''
    [
        [x, y, z, v] list of list of floats
    ]
    '''

    vectors_list = json.loads(vectors_json)
    with open("vectors.txt", "w") as f:
        accumulator = ""
        for vector in vectors_list:
            accumulator += f"{vector[0]} {vector[1]} {vector[2]} {vector[3]}\n"

        accumulator = accumulator.strip("\n")
        f.write(accumulator)
        
    return f"Post {accumulator}"
