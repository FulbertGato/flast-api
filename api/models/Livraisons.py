from app import db

class Livraisons(db.Model):
    __tablename__ = 'livraisons'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=db.func.now())
    status = db.Column(db.String(255), nullable=False)
    commande= db.relationship('Commandes', back_populates='livraison')
    adresse_id = db.Column(db.Integer, db.ForeignKey('adresses.id'), nullable=False)
    adresse = db.relationship('Adresses', back_populates='livraisons', foreign_keys=[adresse_id])
    type_livraison_id = db.Column(db.Integer, db.ForeignKey('type_livraison.id'), nullable=False)
    type_livraison = db.relationship('TypeLivraison', back_populates='livraisons', foreign_keys=[type_livraison_id])

    def __init__(self, date, status, adresse_id, type_livraison_id):
        self.date = date
        self.status = status
        self.adresse_id = adresse_id
        self.type_livraison_id = type_livraison_id
