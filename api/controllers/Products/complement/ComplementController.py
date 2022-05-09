from flask import jsonify
from api.models import Complements
from api.services import generator
from api.services import AuthService
def get_all():
    try :
        complements = Complements.find_all_complements()
        reponse = jsonify(complements),200
        return reponse
            
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


def add(data):
    try :
        if data['token']:
            token = data['token']
            if token:

                gestionnaire = AuthService.get_gestionnaire_by_matricule(token)
                if gestionnaire:
                    name = data['complement']['name']
                    code = generator.generate_product_code('complement')
                    price = data['complement']['price']
                    description = data['complement']['description']
                    status = data['complement']['status']
                    type_complement_id = data['complement']['typeId']
                    complement = Complements.Complements(
                    name=name, 
                    code=code,
                    price=price, 
                    description = description, 
                    status = status, 
                    type_complement_id = type_complement_id)
                    complement = Complements.add_complement(complement)
                    return jsonify(complement.serialize()), 200
            
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
    


def edit(data):
    try :
        if data['token']:
            token = data['token']
            if token:
                gestionnaire = AuthService.get_gestionnaire_by_matricule(token)
                if gestionnaire:
                    id = data['complement']['id']
                    name = data['complement']['name']
                    price = data['complement']['price']
                    description = data['complement']['description']
                    status = data['complement']['status']
                    type_complement_id = data['complement']['typeId']
                    complement = Complements.find_complement_by_id(id)
                    if complement:
                        complement.name = name
                        complement.price = price
                        complement.description = description
                        complement.status = status
                        complement.type_complement_id = type_complement_id
                        complement = Complements.update_complement(id,complement)
                        if complement:
                            return jsonify(complement.serialize()), 200
                        else:
                            return jsonify({"error": "edit failed"}), 400
    except Exception as e :
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials controller'}), 401


def delete(data):
    try :
        if data['token']:
            token = data['token']
            if token:
                gestionnaire = AuthService.get_gestionnaire_by_matricule(token)
                if gestionnaire:
                    id = data['complement']['id']
                    complement = Complements.find_complement_by_id(id)
                    if complement:
                        complement = Complements.delete_complement(id)
                        if complement:
                            return jsonify({"success": "delete success"}), 200
                        else:
                            return jsonify({"error": "delete failed"}), 400
    except Exception as e :
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials controller'}), 401


def get_by_id(data,id):
    try :
        if data['token']:
            token = data['token']
            if token:
                gestionnaire = AuthService.get_gestionnaire_by_matricule(token)
                if gestionnaire:
                    complement = Complements.find_complement_by_id(id)
                    if complement:
                        return jsonify({"success": "get by id success", "complement" : complement.serialize()}), 200
    except Exception as e :
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials controller'}), 401