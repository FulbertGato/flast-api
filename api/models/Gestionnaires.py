from api.models.Users import Users
from app import db

class Gestionnaires(Users):
    __tablename__ = 'gestionnaires'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    matricule = db.Column(db.String(255), nullable=False, unique=True)
    __mapper_args__ = {
        'polymorphic_identity': 'gestionnaires'

    }

    def __init__(self, email, password, first_name, last_name, role_id, matricule):
        super().__init__(email, password, first_name, last_name, role_id)
        self.matricule = matricule

    
    def __repr__(self):
        return '<Gestionnaire %r>' % self.matricule
    
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'prenom': self.first_name,
            'nom': self.last_name,
            'matricule': self.matricule,
            'roleId': self.role_id
        }

#find gestionnaire by matricule
def find_gestionnaire_by_matricule(matricule):
    return Gestionnaires.query.filter_by(matricule=matricule).first()

def add_gestionnaire(gestionnaire):
    db.session.add(gestionnaire)
    db.session.commit()
    return gestionnaire

def get_all_gestionnaires():
    unserelizes =  Gestionnaires.query.all()
    return [unserelize.serialize() for unserelize in unserelizes]


def delete_gestionnaire(gestionnaire):
    db.session.delete(gestionnaire)
    db.session.commit()
    return True

def find_gestionnaire_by_id(id):
    return Gestionnaires.query.filter_by(id=id).first()


def edit_gestionnaire(gestionnaire):
    
    db.session.commit()
    return gestionnaire