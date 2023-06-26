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

if __name__ == "__main__":
    app.run()