from app import db

class Adresses(db.Model):
    __tablename__ = 'adresses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    full_adresse = db.Column(db.String(255), nullable=False)
    indication = db.Column(db.Text , nullable=False)
    zone_id = db.Column(db.Integer, db.ForeignKey('zones.id'), nullable=False)
    zone = db.relationship('Zones', back_populates='adresses', foreign_keys=[zone_id])
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    client = db.relationship('Clients', back_populates='adresses', foreign_keys=[client_id])
    livraisons = db.relationship('Livraisons', back_populates='adresse')

    def __init__(self, name, full_adresse, indication, zone_id, client_id):
        self.name = name
        self.full_adresse = full_adresse
        self.indication = indication
        self.zone_id = zone_id
        self.client_id = client_id