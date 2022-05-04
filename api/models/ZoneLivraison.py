from app import db
class Zones(db.Model):
    __tablename__ = 'zones'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    adresses = db.relationship('Adresses', back_populates='zone')
    price  = db.Column(db.Float, nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'zones'
    }

    def __init__(self, name, price):
        self.name = name
        self.price = price