from flask import Flask
app = Flask(__name__)

@app.route("/sendVector/<int:x>/<int:y>")
def getVector(x, y):
    with open("vectors.txt", "a") as f:
        f.write(f"{x} {y}\n")
    return f"Post {x} {y}"
