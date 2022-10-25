from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  #comment this on deployment
from api.routes import initialize_routes
from config.appconfig import Config
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app, storage
import os

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)  #comment this on deployment
api = Api(app)

basepath = os.path.abspath(os.path.dirname(__file__))
app.config.from_object(Config())

# Initialize Firestore DB
try:
    cred = credentials.Certificate(basepath+"/config/serviceAccountKey.json")

    firebase_admin.initialize_app(cred, {'storageBucket': 'hackmanthan-lostminds.appspot.com'})

    db = firestore.client()
    bucket = storage.bucket()
    print("---------------------------> IN <--------------------------")
except Exception as e:
    print(e)
    print("--------------------------------------> Not Logged in !")



initialize_routes(api)


@app.route("/", strict_slashes=False)
@app.route("/index", strict_slashes=False)
def serve():
    return send_from_directory(app.static_folder, 'index.html')

