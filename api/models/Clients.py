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

    def __repr__(self):
        return '<Client %r>' % self.email
    
    def __str__(self):
        return self.email

    def serealize(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
           
        }

    

def add_client(client):
    db.session.add(client)
    db.session.commit()
    print('client added')
    return client


def get_all_clients():
    clients = Clients.query.all()
    if clients:
        serialized_clients = [client.serealize() for client in clients]
        return serialized_clients
    return False


def delete_client(client):
    
    db.session.delete(client)
    db.session.commit()
    return True
   

def find_client_by_id(id):
    return Clients.query.filter_by(id=id).first()