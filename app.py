import os
from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app = Flask(__name__, static_folder='static', static_url_path='/static')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_object(config)
db = SQLAlchemy(app)

from api.models import Adresses,Produits,Users, Burgers, Clients , Commandes,Complements,TypeComplements,DetailCommandes,Gestionnaires,Livraisons,Menus,Paiements,Roles,TypeLivraison,ZoneLivraison  
db.create_all()
from api.routes.auth import auth_bp
from api.routes.product import product_bp
from api.routes.order import order_bp
@app.route('/')
def hello_world():
    return '<h1>Bienvenue sur Brazil Burger!</h1>'


if __name__ == '__main__':
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/product')
    app.register_blueprint(order_bp, url_prefix='/order')
    app.run(debug=True)
