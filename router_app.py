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
from models.model_users import *

app = Flask(__name__)
cors = CORS(app)


@app.route("/") #Si me pides /
def hello_root():
    return '<h1>Hello ROOT</h1>'

@app.route("/login", methods=['POST'])
def get_logged_user():
    login_data = request.json
    login_email = login_data.get('login_email')
    passw = login_data.get('passw')
    if login_email and passw:
        print ('@#@#@# get_logged_user',login_data, login_email, passw)
    user, token = Users.login(login_email, passw)
    if user:
        return jsonify({'user': user, 'token': token})    
    return jsonify({'message': 'Error en el login ROUTER'})



@app.route("/bands", methods=["GET"])
def get_bands():
    bands, status_code = Band.get_bands()
    return bands, status_code

@app.route("/bands", methods=["POST"])
def post_band():
    band = request.get_json()
    response, status_code = Band.post_band(band)
    return jsonify(response), status_code

@app.route("/bands/<int:band_id>", methods=["GET"])
def get_band(band_id):
    band, status_code = Band.get_band(band_id)
    return jsonify(band), status_code

@app.route("/bands/<int:band_id>", methods=["PUT"])
def put_band(band_id):
    data = request.get_json()
    response, status_code = Band.put_band(data, band_id)
    return jsonify(response), status_code

@app.route("/bands/<int:band_id>", methods=["DELETE"])
def delete_band(band_id):
    response, status_code = Band.delete_band(band_id)
    return jsonify(response), status_code

@app.route("/bands/<int:band_id>", methods=["PATCH"])
def patch_band(band_id):
    data = request.get_json()
    response, status_code = Band.patch_band(data, band_id)
    return jsonify(response), status_code


# CONCERTS
@app.route("/concerts", methods=["GET"])
def get_concerts():
    concerts, status_code = Concert.get_concerts()
    return concerts, status_code

@app.route("/concerts", methods=["POST"])
def post_concert():
    concert = request.get_json()
    response, status_code = Concert.post_concert(concert)
    return jsonify(response), status_code

@app.route("/concerts/<int:concert_id>", methods=["GET"])
def get_concert(concert_id):
    concert, status_code = Concert.get_concert(concert_id)
    return jsonify(concert), status_code

@app.route("/concerts/<int:concert_id>", methods=["PUT"])
def put_concert(concert_id):
    data = request.get_json()
    response, status_code = Concert.put_concert(data, concert_id)
    return jsonify(response), status_code

@app.route("/concerts/<int:concert_id>", methods=["DELETE"])
def delete_concert(concert_id):
    response, status_code = Concert.delete_concert(concert_id)
    return jsonify(response), status_code

@app.route("/concerts/<int:concert_id>", methods=["PATCH"])
def patch_concert(concert_id):
    data = request.get_json()
    response, status_code = Concert.patch_concert(data, concert_id)
    return jsonify(response), status_code

if __name__ == "__main__":
    app.run()