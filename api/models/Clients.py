from api.models.Users import Users
from app import db

class Clients(Users):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    phone = db.Column(db.String(255), nullable=False, unique=True)
    adresses = db.relationship('Adresses', back_populates='client')
    commandes = db.relationship('Commandes', back_populates='client')
    __mapper_args__ = {
        'polymorphic_identity': 'clients'
    }

    def __init__(self, email, password, first_name, last_name, role_id, phone):
        super().__init__(email, password, first_name, last_name, role_id)
        self.phone = phone

    