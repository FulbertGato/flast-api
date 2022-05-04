from api.models.Produits import Produits
from app import db

class Burgers(Produits):
    __tablename__ = 'burgers'
    id = db.Column(db.Integer, db.ForeignKey('produits.id'), primary_key=True)   
    cooking_time = db.Column(db.String(20), nullable=False)
    
    

    __mapper_args__ = {
        'polymorphic_identity': 'burgers'
    }

    def __init__(self, name, code, price, description, status, cooking_time):
        super().__init__(name, code, price, description, status)
        self.cooking_time = cooking_time
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'price': self.price,
            'description': self.description,
            'status': self.status,
            'cookingTime': self.cooking_time
        }

def get_all():
    burgers = Burgers.query.all()
    return [burger.serialize() for burger in burgers]

def add_burger(burger):
    db.session.add(burger)
    db.session.commit()
    return burger


def find_burger_by_id(id):
    return Burgers.query.get(id)


def edit_burger(id, burger):
    burger_to_update = find_burger_by_id(id)
    burger_to_update.name = burger.name
    burger_to_update.price = burger.price
    burger_to_update.description = burger.description
    burger_to_update.status = burger.status
    burger_to_update.cooking_time = burger.cooking_time
    db.session.commit()
    return burger_to_update

def delete_burger(burger):
    db.session.delete(burger)
    db.session.commit()
    return True
        

       