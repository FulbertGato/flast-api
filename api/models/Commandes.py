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