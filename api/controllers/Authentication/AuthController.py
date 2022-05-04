from flask import jsonify
from api.services import AuthService
def login(data):
    try :
        if data['email']  and data['password']:
            login = data['email']
            password = data['password']
            user = AuthService.login(login,password)
            if user:
                if user.role_id == 1:
                    gestionnaire = AuthService.find_gestionnaire_by_id(user.id)
                    return jsonify(gestionnaire), 200
                else :
                    return jsonify({"error": "Acces non autorisé"}), 401
                
                
            return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
    except Exception as e:
        print(e)
    return jsonify({"error": "Acces non autorisé"}), 401

def logout(request):
    pass


def add_gestionnaire(data):
    try :
        matricule = data['token']
        if matricule:
            #select gestionnaire who has this matricule
            gestionnaire = AuthService.get_gestionnaire_by_matricule(matricule)
            if gestionnaire:
                gestionnaireCreate = AuthService.add_gestionnaire(data['gestionnaire'])
                if gestionnaireCreate:
                    return jsonify(gestionnaireCreate), 200
                return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
            return jsonify({"error": "Acces non autorisé"}), 401
    except Exception as e:
        print(e)
    return jsonify({"error": "Acces non autorisé"}), 401

def get_all_gestionnaires(token):
    try :
        if token:
            #select gestionnaire who has this matricule
            gestionnaire = AuthService.get_gestionnaire_by_matricule(token) 
            if gestionnaire:
                gestionnaires = AuthService.get_all_gestionnaires()
                if gestionnaires:
                    return jsonify(gestionnaires), 200
            return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
    except Exception as e:
        print(e)
    return jsonify({"error": "Acces non autorisé"}), 401


def delete_gestionnaire(token, id):
    try :
        if token:
            #select gestionnaire who has this matricule
            gestionnaire = AuthService.get_gestionnaire_by_matricule(token) 
            if gestionnaire:
                gestionnaireDelete = AuthService.delete_gestionnaire(id)
                if gestionnaireDelete:
                    return jsonify({"status" : "success"}), 200
            return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
    except Exception as e:
        print(e)
    return jsonify({"error": "Acces non autorisé"}), 401



def edit_gestionnaire(data):
    try :
        matricule = data['token']
        if matricule:
            #select gestionnaire who has this matricule
            gestionnaire = AuthService.get_gestionnaire_by_matricule(matricule) 
            if gestionnaire:
                gestionnaireEdit = AuthService.edit_gestionnaire(data['gestionnaire'])
                if gestionnaireEdit:
                    return jsonify(gestionnaireEdit), 200
            return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
    except Exception as e:
        print(e)
    return jsonify({"error": "Acces non autorisé"}), 401