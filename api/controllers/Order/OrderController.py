from flask import jsonify
from api.models import Commandes, DetailCommandes ,Produits 
from api.services import AuthService
from api.services import generator

def create_order(data):
    try:
        number=generator.generate_product_code('commande')
        status='en attente'
        client_id = data['client_id']
        total = data['total']
        commande = Commandes.Commandes(number=number, status=status, client_id=client_id, total=total)
        commande =  Commandes.add_commande(commande)
        if commande:       
            #cree detail commande
            for detail in data['detail_commandes']:
                #find produc by code
                produit =Produits.find_by_code(detail['code'])
                if produit:
                    detail = DetailCommandes.DetailCommandes(commande_id=commande.id,produit_id=produit.id,quantity=detail['quantity'],price = detail['price'])
                    detail = DetailCommandes.add_detail_commande(detail)
                    #return jsonify(commande.serealize()), 200   
                
            return jsonify(commande.serealize()), 200 
                      
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}),401
    return jsonify({'error': 'error'}), 500

def get_all_orders():
    try:
        orders = Commandes.get_all_orders()
        if orders:   
            return jsonify(orders), 200
    except Exception as e:
        print(e)
    return jsonify({'error': 'error'}), 500


def get_order(id):
    try:
        order = Commandes.get_order_by_id(id)
        if order:   
            return jsonify(order), 200
    except Exception as e:
        print(e)
    return jsonify({'error': 'error'}), 500

def get_order_by_client(id):
    try:
        order = Commandes.get_order_by_client_id(id)
        if order:   
            return jsonify(order), 200
    except Exception as e:
        print(e)
    return jsonify({'error': 'error'}), 500

def update_order(id, status):
    try:
        order = Commandes.get_order_by_id(id)
        if order:
            return Commandes.update(id,status)
    except Exception as e:
        print(e)
    return jsonify({'error': 'error'}), 500
