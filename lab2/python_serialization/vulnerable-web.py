import pickle
import base64
from flask import Flask, request
app = Flask(__name__)
@app.route("/vulnerable", methods=["POST"])
def vulnerableapp():
    form_data = base64.urlsafe_b64decode(request.form['hack'])
    deserialized = pickle.loads(form_data)
    return 'deserialized', 204