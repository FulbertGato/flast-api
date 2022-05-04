from app import db
class DetailCommandes(db.Model):
    __tablename__ = 'detail_commandes'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    commande_id = db.Column(db.Integer, db.ForeignKey('commandes.id'), nullable=False)
    commandes = db.relationship('Commandes', back_populates='detail_commandes', foreign_keys=[commande_id])
    produit_id = db.Column(db.Integer, db.ForeignKey('produits.id'), nullable=False)
    produit = db.relationship('Produits', back_populates='detail_commandes', foreign_keys=[produit_id])

    def __init__(self, quantity, price, commande_id, produit_id):
        self.quantity = quantity
        self.price = price
        self.commande_id = commande_id
        self.produit_id = produit_id
    