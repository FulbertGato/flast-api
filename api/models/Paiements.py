from app import db

class Paiements(db.Model):
    __tablename__ = 'paiements'
    id = db.Column(db.Integer, primary_key=True)
    paiement_id = db.Column(db.Integer, nullable=False, unique=True)
    method = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=db.func.now())
    status = db.Column(db.String(255), nullable=False)
    commande= db.relationship('Commandes', back_populates='paiement')
    total = db.Column(db.Float, nullable=False)

    def __init__(self, paiement_id, method, status, total):
        self.paiement_id = paiement_id
        self.method = method
        self.status = status
        
        self.total = total
   