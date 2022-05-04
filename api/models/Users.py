from app import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role = db.relationship('Roles', back_populates='users')
    create_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    type = db.Column(db.String(255), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'users',
        'polymorphic_on': type
    }

    def __init__(self, email, password, first_name, last_name, role_id):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.role_id = role_id

def find_user_by_email(email):
    return Users.query.filter_by(email=email).first()
