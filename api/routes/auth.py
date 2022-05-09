from flask import Blueprint, jsonify, request
from api.controllers.Authentication import AuthController
from app import app

auth_bp = Blueprint('auth_bp', __name__)


@app.route('/api/auth/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.get_json()         
            return AuthController.login(data)     
        except Exception as e:
            pass
    return jsonify({"error": "Bad request"}), 400


@app.route('/api/auth/ges', methods=['POST'])
def add_gestionnaire():
    try :
        data = request.get_json()
        return AuthController.add_gestionnaire(data)
    except Exception as e:
        print (e)
    return jsonify({"error": "Bad request"}), 400


@app.route('/api/auth/gestionnaires/<string:token>', methods=['GET'])
def get_all_gestionnaires(token):
    try :
        return AuthController.get_all_gestionnaires(token)
    except Exception as e:
        print (e)
    return jsonify({"error": "Bad request"}), 400

@app.route('/api/auth/gestionnaires/<string:token>/<int:id>', methods=['DELETE'])
def delete_gestionnaire(token, id):
    try :
        return AuthController.delete_gestionnaire(token, id)
    except Exception as e:
        print (e)
    return jsonify({"error": "Bad request"}), 400
@app.route('/api/auth/ges', methods=['PUT'])
def edit_gestionnaire():
    try :
        data = request.get_json()
        return AuthController.edit_gestionnaire(data)
    except Exception as e:
        print (e)
    return jsonify({"error": "Bad request"}), 400


#add client
@app.route('/api/auth/client', methods=['POST'])
def add_client():
    try :
        data = request.get_json()
        return AuthController.add_client(data)
    except Exception as e:
        print (e)
#create role 
@app.route('/api/auth/role', methods=['POST'])
def add_role():
    try :
        data = request.get_json()
        return AuthController.add_role(data)
    except Exception as e:
        print (e)

    return jsonify({"error": "Bad request"}), 400


#get all clients 
@app.route('/api/auth/clients/<string:token>', methods=['GET'])
def get_all_clients(token):
    try :
        return AuthController.get_all_clients(token)
    except Exception as e:
        print (e)
    return jsonify({"error": "Bad request"}), 400


#delete client
@app.route('/api/auth/clients/<string:token>/<int:id>', methods=['DELETE'])
def delete_client(token, id):
    try :
        return AuthController.delete_client(token, id)
    except Exception as e:
        print (e)

