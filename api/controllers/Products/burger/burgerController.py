from flask import jsonify
from api.models import Burgers
from api.services import generator
def get_all_burger():
    try:
        burgers = Burgers.get_all()
        if burgers:
            respones = jsonify(burgers), 200
            return respones
        else:
            return jsonify({"error": "get all burger failed"}), 400
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


def add(data):
    try:
        if data['token']:
            token = data['token']
            if token:
                name = data['burger']['name']
                code = generator.generate_product_code('burger')
                price = data['burger']['price']
                description = data['burger']['description']
                status = data['burger']['status']
                time = data['burger']['time']
                burger = Burgers.Burgers(name=name, code=code, price=price, description=description, status=status, cooking_time=time)
                burger = Burgers.add_burger(burger)
                if burger:
                    return jsonify(burger.serialize()), 200
                else:
                    return jsonify({"error": "add failed"}), 400
    except Exception as e:
        print("exception: ", e)
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


def edit(data):
    try:
        if data['token']:
            token = data['token']
            if token:
                id = data['burger']['id']
                name = data['burger']['name']
                price = data['burger']['price']
                description = data['burger']['description']
                status = data['burger']['status']
                time = data['burger']['time']
                burger = Burgers.find_burger_by_id(id)
                if burger:
                    burger.name = name
                    burger.price = price
                    burger.description = description
                    burger.status = status
                    burger.cooking_time = time
                    burger = Burgers.edit_burger(id,burger)
                    if burger:
                        return jsonify({"success": "edit success", "burger" : burger.serialize()}), 200
                    else:
                        return jsonify({"error": "edit failed"}), 400
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401


def delete(data):
    try:
        if data['token']:
            token = data['token']
            if token:
                id = data['burger']['id']
                burger = Burgers.find_burger_by_id(id)
                if burger:
                    burger = Burgers.delete_burger(burger)
                    if burger:
                        return jsonify({"success": "delete success"}), 200
                    else:
                        return jsonify({"error": "delete failed"}), 400
    except Exception as e:
        print(e)
    return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401