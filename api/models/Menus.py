from api.models.Produits import Produits
from app import db 

menus_complements = db.Table('menus_complements', db.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('menus_id', db.ForeignKey('menus.id')),
    db.Column('complements_id', db.ForeignKey('complements.id'))
)
class Menus (Produits):
    __tablename__ = 'menus'
    id = db.Column(db.Integer, db.ForeignKey('produits.id'), primary_key=True)
    cooking_time = db.Column(db.String(10), nullable=False)
    burger_id = db.Column(db.Integer, db.ForeignKey('burgers.id'), nullable=False)
    burger = db.relationship('Burgers', backref='menus',foreign_keys=[burger_id])
    complements = db.relationship('Complements', back_populates='menus', secondary='menus_complements')
    image=db.Column(db.String(100), nullable=True)


    __mapper_args__ = {
        'polymorphic_identity': 'menus'
    }

    def __init__(self, name, code, price, description, status, cooking_time, burger_id, complements, image):
        super().__init__(name, code, price, description, status)
        self.cooking_time = cooking_time
        self.burger_id = burger_id
        self.complements = complements
        self.image = image

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'price': self.price,
            'description': self.description,
            'status': self.status,
            'cookingTime': self.cooking_time,
            'burger': self.burger.name,
            'burgerObject': self.burger.serialize(),
            'complements': [complement.serialize() for complement in self.complements],
            'image': self.image
        }


def get_all():
    menus = Menus.query.all()
    return [menu.serialize() for menu in menus]


def add_menu(menu):
    db.session.add(menu)
    db.session.commit()
    return menu
def find_menu_by_id(id):
    menu = Menus.query.filter_by(id=id).first()
    return menu.serialize()

def edit_menu(menu):
    db.session.commit()
    return menu


def delete_menu(menu):
    db.session.delete(menu)
    db.session.commit()
    return menu
