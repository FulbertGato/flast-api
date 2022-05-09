from app import db

class Commandes(db.Model):
    __tablename__ = 'commandes'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(255), nullable=False, unique=True)
    date = db.Column(db.DateTime, nullable=False, default=db.func.now())
    status = db.Column(db.String(255), nullable=False)
    detail_commandes = db.relationship('DetailCommandes', back_populates='commandes')
    paiement_id = db.Column(db.Integer, db.ForeignKey('paiements.id'), nullable=True)
    paiement = db.relationship('Paiements', back_populates='commande', foreign_keys=[paiement_id])
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    client = db.relationship('Clients', back_populates='commandes', foreign_keys=[client_id])
    livraison_id = db.Column(db.Integer, db.ForeignKey('livraisons.id'), nullable=True)
    livraison = db.relationship('Livraisons', back_populates='commande', foreign_keys=[livraison_id])
    total = db.Column(db.Float, nullable=False)

    def __init__(self, number,  status, client_id, total):
        self.number = number
        self.status = status
        self.client_id = client_id
        self.total = total

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self
    
    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.save()
        return self

    def serealize(self):
        return {
            'id': self.id,
            'number': self.number,
            'date': self.date,
            'status': self.status,
            'detail_commandes': [detail.serialize() for detail in self.detail_commandes],
            'paiement': self.paiement.serialize() if self.paiement else None,
            'client': self.client.serealize() if self.client else None,
            'livraison': self.livraison.serialize() if self.livraison else None,
            'total': self.total,
            
        }


def add_commande(commande):
    db.session.add(commande)
    db.session.commit()
    return commande


def get_all_orders():
    commandes = Commandes.query.all()
    print("okiii")
    return [commande.serealize() for commande in commandes]

def get_order_by_id(id):
    print("okiii")
    commande = Commandes.query.get(id)
    #delete commande

    #db.session.delete(commande)
    #db.session.commit()

    return commande.serealize()


def get_order_by_client_id(id):
    commandes = Commandes.query.filter_by(client_id=id).all()
    return [commande.serealize() for commande in commandes]


def update(id,status):
    commande = Commandes.query.filter_by(id=id).first()
    commande.status = status

    db.session.commit()
    return commande.serealize()