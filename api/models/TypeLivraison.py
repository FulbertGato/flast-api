from app import db

class TypeLivraison(db.Model):
    __tablename__ = 'type_livraison'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    livraisons = db.relationship('Livraisons', back_populates='type_livraison')

    def __init__(self, name):
        self.name = name