from flask import Flask, request, jsonify
from flask_cors import CORS
from models.bands_model import *
#get_all_bands, get_band_by, post_band, put_band, del_band
from models.concerts_model import *
#get_all_concerts, get_concert_by, post_concert, put_concert, del_concert
from models.shifts_model import *
#get_all_shifts, get_shift_by, post_shift, put_shift, del_shift
from models.stages_model import *
#get_all_stages, get_stage_by, post_stage, put_stage, del_stage

app = Flask(__name__)
cors = CORS(app)

@app.route("/") #Si me pides /
def hello_root():
    return '<h1>Hello ROOT</h1>'