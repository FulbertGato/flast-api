from flask import Blueprint, jsonify, request
from app import app
from api.services import AuthService
from api.controllers.Order import OrderController
order_bp = Blueprint('order_bp', __name__)


@app.route('/api/order/', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        return OrderController.create_order(data)
        
    except Exception as e:
        return jsonify({'error': str(e)})
    return jsonify({'error': 'error'}), 500


@app.route('/api/orders/<string:token>/<int:id>', methods=['GET'])
def get_order(id,token):
    try:
        if token:
            #select gestionnaire who has this matricule
            gestionnaire = AuthService.get_gestionnaire_by_matricule(token)
            if gestionnaire:
                return OrderController.get_order(id)
                
        return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
    except Exception as e:
        print(e)
    return jsonify({"error": "Acces non autorisé"}), 401
#get all orders
@app.route('/api/orders/<string:token>', methods=['GET'])
def get_all_orders(token):
    try:
        if token:
            #select gestionnaire who has this matricule
            gestionnaire = AuthService.get_gestionnaire_by_matricule(token)
            if gestionnaire:
                return  OrderController.get_all_orders()
                
            return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
    except Exception as e:
        print(e)
    return jsonify({"error": "Acces non autorisé"}), 401

@app.route('/api/order/client', methods=['POST'])
def get_order_by_client():
    try:
        data = request.get_json()
        return OrderController.get_order_by_client(data['client_id'])

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})
    return jsonify({'error': 'error'}), 500


@app.route('/api/orders/<string:token>/<int:id>/<string:status>', methods=['GET'])
def update_order(id,status,token):
    try:
        if token:
            #select gestionnaire who has this matricule
            gestionnaire = AuthService.get_gestionnaire_by_matricule(token)
            if gestionnaire:
                return OrderController.update_order(id,status)        
            return jsonify({'status': 'error', 'message': 'Invalid Credentials'}), 401
    except Exception as e:
        print(e)
    return jsonify({"error": "Acces non autorisé"}), 401
