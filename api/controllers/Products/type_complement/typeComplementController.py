from flask import jsonify
from api.models import TypeComplements
from api.services import AuthService
def get_all():
    try :
        
        types = TypeComplements.find_all_type_complements()
        if types:
            response = jsonify(types), 200
            
            return response
        else:
            return jsonify({"error": "Aucune donnée disponible"}), 400               
    except Exception as e:
        print(e)
        
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401




def add_type(data):
    try:
       if data['token']:
            token = data['token']
            matricule = token
            if matricule:
                #select gestionnaire who has this matricule
                gestionnaire = AuthService.get_gestionnaire_by_matricule(matricule)
                if gestionnaire:
                    name = data['type']['name']
                    image = data['type']['image']

                    typeComplement = TypeComplements.TypeComplements(name=name,image=image)
                    typeComplement = TypeComplements.create_type_complement(typeComplement)
                    if typeComplement:
                        response = jsonify(typeComplement), 200
                        return response
                    else:
                        return jsonify({"status": "error"}), 400

    except Exception as e:
        print (e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials controller'}), 401


def edit_type(data):
    try:
        if data['token']:
            token = data['token']
            matricule = token
            if matricule:
                #select gestionnaire who has this matricule
                gestionnaire = AuthService.get_gestionnaire_by_matricule(matricule)
                if gestionnaire:
                    id = data['type']['id']
                    name = data['type']['name']
                    image = data['type']['image']
                    typeComplement = TypeComplements.find_type_complement_by_id(id)
                    if typeComplement:
                        typeComplement.name = name
                        typeComplement.image = image
                        typeComplement = TypeComplements.update_type_complement(id,typeComplement)
                        if typeComplement:
                            return jsonify({"success": "edit type success", "type" : typeComplement.serialize()}), 200
                        else:
                            return jsonify({"error": "edit type failed"}), 400
    except Exception as e :
        pass
    return jsonify({'status': 'error', 'message': 'Invalid Credentials controller'}), 401


def delete_type(data):
    try:
        if data['token']:
            token = data['token']
            matricule = token
            if matricule:
                #select gestionnaire who has this matricule
                gestionnaire = AuthService.get_gestionnaire_by_matricule(matricule)
                if gestionnaire:
                    id = data['type']['id']
                    typeComplement = TypeComplements.find_type_complement_by_id(id)
                    if typeComplement:
                        typeComplement = TypeComplements.delete_type_complement(id)
                        if typeComplement:
                            return jsonify({"success": "delete type success"}), 200
                        else:
                            return jsonify({"error": "delete type failed"}), 400
    except Exception as e :
        pass
    return jsonify({'status': 'error', 'message': 'Invalid Credentials controller'}), 401


def get_type(data, id):
    try:
        if data['token']:
            token = data['token']
            if token:
                typeComplement = TypeComplements.find_type_complement_by_id(id)
                if typeComplement:
                    return jsonify({"success": "get type success", "type" : typeComplement.serialize()}), 200
    except Exception as e :
        pass
    return jsonify({'status': 'error', 'message': 'Invalid Credentials controller'}), 401


def get_type_by_name(data, name):
    try:
        if data['token']:
            token = data['token']
            if token:
                typeComplement = TypeComplements.find_type_complement_by_name(name)
                if typeComplement:
                    return jsonify({"success": "get type success", "type" : typeComplement.serialize()}), 200
    except Exception as e :
        pass
    return jsonify({'status': 'error', 'message': 'Invalid Credentials controller'}), 401