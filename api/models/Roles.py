from app import db

class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    users = db.relationship('Users', back_populates='role')

    def __init__(self, name):
        self.name = name

    def serealize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

def create_role(name):
    role = Roles(name)
    #select role by name
    #role = Roles.query.filter_by(name=name).first()
    #select role by id
   # role = Roles.query.filter_by(id=3).first()


    db.session.add(role)
    db.session.commit()
    return role.serealize()