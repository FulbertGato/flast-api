
from unicodedata import name

from sqlalchemy import false
from api.models import Roles

from api.services import generator
from api.models import Users, Gestionnaires, Clients


def login(login,password):
    user = Users.find_user_by_email(login)
    if user:
        if user.password == password:
            return user
    return False

def get_gestionnaire_by_matricule(matricule):
    gestionnaire = Gestionnaires.find_gestionnaire_by_matricule(matricule)
    if gestionnaire:
        return gestionnaire.serialize()
    return  False


#add gestionnaire
def add_gestionnaire(data):
    matricule = generator.generate_product_code('gestionnaire')
    email= data['email']
    password = data['password']
    first_name = data['nom']
    last_name = data['prenom']
    role_id = 1

    gestionnaire = Gestionnaires.Gestionnaires(email=email, password=password, first_name=first_name, last_name=last_name, role_id=role_id, matricule=matricule)
    gestionnaire = Gestionnaires.add_gestionnaire(gestionnaire)
    return gestionnaire.serialize()

def get_all_gestionnaires():
    gestionnaires = Gestionnaires.get_all_gestionnaires()
    if gestionnaires:
        return gestionnaires
    return False

def delete_gestionnaire(id):
    gestionnaire = Gestionnaires.find_gestionnaire_by_id(id)
    if gestionnaire:
        Gestionnaires.delete_gestionnaire(gestionnaire)
        return True
    return False

def edit_gestionnaire(data):
    gestionnaire = Gestionnaires.find_gestionnaire_by_id(data[id])
    if gestionnaire:
        gestionnaire.email = data['email']
        gestionnaire.password = data['password']
        gestionnaire.first_name = data['nom']
        gestionnaire.last_name = data['prenom']
        gestionnaire = Gestionnaires.edit_gestionnaire(gestionnaire)
        return gestionnaire.serialize()
    return False

def find_gestionnaire_by_id(id):
    gestionnaire = Gestionnaires.find_gestionnaire_by_id(id)
    if gestionnaire:
        return gestionnaire.serialize()
    return False

def create_role():
    role = Roles.create_role(name='client')
    print ("haha")
    return role

def add_client(data):
    #matricule = generator.generate_product_code('user')
    email= data['email']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']
    phone = data['phone']
    role_id = 2

    client = Clients.Clients(email=email, password=password, first_name=first_name, last_name=last_name,phone=phone, role_id=role_id)
    client = Clients.add_client(client)
    return client.serealize()


def get_all_clients():
    clients = Clients.get_all_clients()
    if clients:
        
        return clients
    return False

def delete_client(id):
    client = Clients.find_client_by_id(id)
    if client:
        Clients.delete_client(client)
        return True
    return False

def find_client_by_id(id):
    client = Clients.find_client_by_id(id)
    if client:
        return client.serealize()