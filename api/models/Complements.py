from api.models.Produits import Produits

from app import db
class Complements(Produits):
    __tablename__ = 'complements'
    id = db.Column(db.Integer, db.ForeignKey('produits.id'), primary_key=True)
    type_complement_id = db.Column(db.Integer, db.ForeignKey('type_complements.id'), nullable=False)
    type_complement = db.relationship('TypeComplements', back_populates='complements', foreign_keys=[type_complement_id])
    menus = db.relationship('Menus', back_populates='complements', secondary='menus_complements')

    __mapper_args__ = {
        'polymorphic_identity': 'complements'       
    }

    def __init__(self, name, code, price, description, status, type_complement_id):
        super().__init__(name, code, price, description, status)
        self.type_complement_id = type_complement_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'price': self.price,
            'description': self.description,
            'status': self.status,
            'typeComplementName': self.type_complement.name
        }

def find_all_complements():
    complements = Complements.query.all()
    serialize_complements = [complement.serialize() for complement in complements]
    return serialize_complements

def add_complement(complement):
    db.session.add(complement)
    db.session.commit()
    return complement


def find_complement_by_id(id):
    return Complements.query.get(id)


def update_complement(id, complement):
    complement_to_update = find_complement_by_id(id)
    complement_to_update.name = complement.name
    complement_to_update.price = complement.price
    complement_to_update.description = complement.description
    complement_to_update.status = complement.status
    db.session.commit()
    return complement_to_update

def delete_complement(id):
    complement_to_delete = find_complement_by_id(id)
    db.session.delete(complement_to_delete)
    db.session.commit()
    return True