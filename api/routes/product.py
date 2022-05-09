import os
from flask import Blueprint, jsonify, request
from api.controllers.Products.type_complement import typeComplementController
from api.controllers.Products.complement import ComplementController
from api.controllers.Products.burger import burgerController
from api.controllers.Products.menu import menuController
from api.services.generator import generate_product_code
from app import app
from werkzeug.utils import secure_filename
from config.config import basedir
UPLOAD_FOLDER ='api\static\images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
product_bp = Blueprint('product_bp', __name__)

@app.route('/api/type/complement', methods=['GET'])
def get_all_type_complement():
    try:
        return typeComplementController.get_all()
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401



@app.route('/api/type/complement', methods=['POST'])
def add_type_complement():
    try:
        data = request.get_json()

        return typeComplementController.add_type(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


@app.route('/api/type/complement', methods=['PUT'])
def edit_type_complement():
    try:
        data = request.get_json()
        return typeComplementController.edit_type(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401

@app.route('/api/type/complement/<int:id>', methods=['PUT'])
def edit_type():
    try:
        data = request.get_json()
        return typeComplementController.edit_type(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401

@app.route('/api/type/complement', methods=['DELETE'])
def delete_type_complement():
    try:
        data = request.get_json()
        return typeComplementController.delete_type(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401

@app.route('/api/type/complement/<string:token>/<int:id>', methods=['DELETE'])
def delete_type(id, token):
    try:
        data = {'type': {'id' : id}, 'token': token}
        return typeComplementController.delete_type(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
#get one type complement

@app.route('/api/type/complement/<int:id>', methods=['GET'])
def get_type_complement(id):
    try:
        data = request.get_json()
        return typeComplementController.get_type(data, id)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401

#get one type complement by name
@app.route('/api/type/complement/<string:name>', methods=['GET'])
def get_type_complement_by_name(name):
    try:
        data = request.get_json()
        return typeComplementController.get_type_by_name(data, name)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401



#get all complement 
@app.route('/api/complement', methods=['GET'])
def get_all_complement():
    try:
        return ComplementController.get_all()
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401

#add complement
@app.route('/api/complement', methods=['POST'])
def add_complement():
    try:
        data = request.get_json()
        return ComplementController.add(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


#edit complement
@app.route('/api/complement', methods=['PUT'])
def edit_complement():
    try:
        data = request.get_json()
        return ComplementController.edit(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


#delete complement
@app.route('/api/complement', methods=['DELETE'])
def delete_complement():
    try:
        data = request.get_json()
        return ComplementController.delete(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401

@app.route('/api/complement/<string:token>/<int:id>', methods=['DELETE'])
def delete_complement_by_id(id, token):
    try:
        data = {'complement': {'id' : id}, 'token': token}
        return ComplementController.delete(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
#get one complement
@app.route('/api/complement/<int:id>', methods=['GET'])
def get_complement(id):
    try:
        data = request.get_json()
        return ComplementController.get_by_id(data, id)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401



# get all burger
@app.route('/api/burger', methods=['GET'])
def get_all_burger():
    try:

        return burgerController.get_all_burger()
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


#add burger
@app.route('/api/burger', methods=['POST'])
def add_burger():
    try:
        data = request.get_json()
        return burgerController.add(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


#edit burger
@app.route('/api/burger', methods=['PUT'])
def edit_burger():
    try:
        data = request.get_json()
        return burgerController.edit(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


#delete burger
@app.route('/api/burger', methods=['DELETE'])
def delete_burger():
    try:
        data = request.get_json()
        return burgerController.delete(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
#delete burger
@app.route('/api/burger/<string:token>/<int:id>', methods=['DELETE'])
def delete_burger_by_id(token,id):
    try:
        data = {'burger': {'id' : id}, 'token': token}
        return burgerController.delete(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


#all menu
@app.route('/api/menu', methods=['GET'])
def get_all_menu():
    try:

        return menuController.get_all_menu()
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


#add menu
@app.route('/api/menu', methods=['POST'])
def add_menu():
    try:
        data = request.get_json()
        return menuController.add(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


#edit menu
@app.route('/api/menu', methods=['PUT'])
def edit_menu():
    try:
        data = request.get_json()
        return menuController.edit(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


#delete menu
@app.route('/api/menu', methods=['DELETE'])
def delete_menu():
    try:
        data = request.get_json()
        return menuController.delete(data)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


@app.route('/api/media/upload', methods=['POST'])
def upload_file():
    
    if request.method == 'POST':
        
        try:
                # check if the post request has the file part
            if 'file'  in request.files:
                return jsonify({'status': 'not files'}), 401
            file = request.files.get('file')
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                return jsonify({'status': 'error'}), 401
            if file:
                filename = secure_filename(file.filename)
                print(filename)
                #get extension
                extension = filename.rsplit('.', 1)[1]
                #get name
                name = generate_product_code('image')
                fullname=name+'.'+extension
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], fullname))
                print("je suis arriver")
                return jsonify({'fullname':fullname}), 200
        except Exception as e:
            print(e)


#get menu by id 
@app.route('/api/menu/<int:id>', methods=['GET'])
def get_menu(id):
    try:
        
        return menuController.get_by_id(id)
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401