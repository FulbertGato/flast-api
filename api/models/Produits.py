from app import db
class Produits(db.Model):
    __tablename__ = 'produits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    code = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    detail_commandes = db.relationship('DetailCommandes', back_populates='produit')
    type = db.Column(db.String(255), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'produits',
        'polymorphic_on': type
    }

    def __init__(self, name, code, price, description, status):
        self.name = name
        self.code = code
        self.price = price
        self.description = description
        self.status = status


def find_by_code(code):
    return Produits.query.filter_by(code=code).first()