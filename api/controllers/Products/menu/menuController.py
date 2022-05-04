from flask import jsonify
from api.models import Menus
from api.models import Complements
from api.models import Burgers
from api.services import generator
def get_all_menu():
    try:
        menus = Menus.get_all()
        if menus:
            responses = jsonify(menus), 200
            return responses
        else:
            return jsonify({"error": "get all menu failed"}), 400
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


def add(data):
    try:
        if data['token']:
            token = data['token']
            if token:
                name = data['menu']['name']
                code = generator.generate_product_code('menu')
                description = data['menu']['description']
                status = data['menu']['status']
                
                burger_id = data['menu']['burgerId']
                complementsId = data['menu']['complementsId']
                i=0
                prix = 0.0
                complements = []
                for i in complementsId:
                    print(i)
                    complement = Complements.find_complement_by_id(i)
                    prix += complement.price
                    complements.append(complement)
                    
                burger = Burgers.find_burger_by_id(burger_id)
                price = prix + float(burger.price)
                cooking_time = burger.cooking_time
                menu = Menus.Menus(name=name, code=code, price=price, description=description, status=status, cooking_time = cooking_time, burger_id = burger_id, complements=complements)
                menu = Menus.add_menu(menu)
                if menu:
                    return jsonify({"success": "add menu success", "menu" : menu.serialize()}), 200
                else:
                    return jsonify({"error": "add menu failed"}), 400
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


def edit(data):
    try:
        if data['token']:
            token = data['token']
            if token:
                id = data['menu']['id']
                name = data['menu']['name']
                description = data['menu']['description']
                status = data['menu']['status']
                burger_id = data['menu']['burgerId']
                complementsId = data['menu']['complementsId']
                i=0
                prix = 0.0
                complements = []
                for i in complementsId:
                    print(i)
                    complement = Complements.find_complement_by_id(i)
                    prix += complement.price
                    complements.append(complement)
                    
                burger = Burgers.find_burger_by_id(burger_id)
                price = prix + float(burger.price)
                cooking_time = burger.cooking_time
                menu = Menus.find_menu_by_id(id)
                if menu:
                    menu.name = name
                    menu.description = description
                    menu.status = status
                    menu.burger_id = burger_id
                    menu.price = price
                    menu.cooking_time = cooking_time
                    menu.complements = complements
                    menu = Menus.edit_menu(menu)
                    if menu:
                        return jsonify({"success": "edit menu success", "menu" : menu.serialize()}), 200
                    else:
                        return jsonify({"error": "edit menu failed"}), 400
                
                
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


def delete(data):
    try:
        if data['token']:
            token = data['token']
            if token:
                id = data['menu']['id']
                menu = Menus.find_menu_by_id(id)
                if menu:
                    menu = Menus.delete_menu(menu)
                    if menu:
                        return jsonify({"success": "delete menu success"}), 200
                    else:
                        return jsonify({"error": "delete menu failed"}), 400
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401

def get_by_id(id):
    try:
        menu = Menus.find_menu_by_id(id)
        if menu:
            return jsonify(menu), 200
        else:
            return jsonify({'status': 'gatoError'}), 200
    except Exception as e:
        print(e)
    return jsonify({'status': 'gatoError'}), 200