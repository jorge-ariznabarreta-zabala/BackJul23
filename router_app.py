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

#BANDS
@app.route("/bands", methods=['GET'])#Si me pides /bands con GET
def get_bands():
    bands = Band.get_all_bands()
    
    # Aquí debes procesar la lista de bandos y devolverla como una respuesta adecuada, por ejemplo:
    return bands

@app.route("/bands/<band_id>", methods=['GET']) #Si me pides /bands/ALGO con GET
def get_band(band_id):
    band = Band.get_band_by_id(band_id)
    print("@#@#@#@#L44 router_app.py", band)
    if band:        
        return band
    else:
    # Si no se encuentra el bando, puedes devolver un mensaje de error o una respuesta vacía
        return jsonify({'message': 'banda no encontrado'})


@app.route("/bands", methods=["POST"]) #Si me pides /bands con POST
def create_band():
    data= request.get_json()
    print ('**createband', data)
    Band.post_band(data)
    response = {'message': 'band created successfully'}
    return jsonify(response), 200

@app.route("/bands/<band_id>", methods=["PUT"])
def update_band(band_id):
    data = request.get_json()
    print('**update_band', data['id'])
    result = Band.put_band(data, band_id)
    if isinstance(result, str):
        return jsonify({"message": result})
    else:
        return jsonify({"message": "band updated successfully"})

@app.route("/bands/<band_id>", methods=["PATCH"])
def patch_band(band_id):
    data = request.get_json()
    result = Band.patch_band(data, band_id)
    if isinstance(result, str):
        return jsonify({"message": result})
    else:
        return jsonify({"message": "band updated successfully"})   

@app.route("/bands/<band_id>", methods=['DELETE'])#Si me pides /bands/ALGO con DELETE
def delete_band(band_id): 
    Band.delete_band(band_id)
    response = {'message': 'band deleted successfully'}
    return jsonify(response), 200

# CONCERTS
@app.route("/concerts", methods=['GET'])#Si me pides /concerts con GET
def get_concerts():
    concerts = Concert.get_all_concerts()
    
    # Aquí debes procesar la lista de concertos y devolverla como una respuesta adecuada, por ejemplo:
    return concerts

@app.route("/concerts/<concert_id>", methods=['GET']) #Si me pides /concerts/ALGO con GET
def get_concert(concert_id):
    
    concert = Concert.get_concert_by_id(concert_id)
    if concert:        
        return jsonify(concert)
    else:
    # Si no se encuentra el concerto, puedes devolver un mensaje de error o una respuesta vacía
        return jsonify({'message': 'concerta no encontrado'})


@app.route("/concerts", methods=["POST"]) #Si me pides /concerts con POST
def create_concert():
    data= request.get_json()
    print ('**createconcert', data)
    Concert.post_concert(data)

    response = {'message': 'concert created successfully'}
    return jsonify(response), 200

@app.route("/concerts/<concert_id>", methods=["PUT"])
def update_concert(concert_id):
    data = request.get_json()
    print('**update_concert', data['id'])
    result = Concert.put_concert(data, concert_id)
    if isinstance(result, str):
        return jsonify({"message": result})
    else:
        return jsonify({"message": "concert updated successfully"})

@app.route("/concerts/<concert_id>", methods=["PATCH"])
def patch_concert(concert_id):
    data = request.get_json()
    result = Concert.patch_concert(data, concert_id)
    if isinstance(result, str):
        return jsonify({"message": result})
    else:
        return jsonify({"message": "concert updated successfully"})   

@app.route("/concerts/<concert_id>", methods=['DELETE'])#Si me pides /concerts/ALGO con DELETE
def delete_concert(concert_id): 
    Concert.delete_concert(concert_id)
    response = {'message': 'concert deleted successfully'}
    return jsonify(response), 200