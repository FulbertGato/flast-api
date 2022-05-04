

from app import db

class TypeComplements(db.Model):
    __tablename__ = 'type_complements'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    image = db.Column(db.String(255), nullable=True, unique=True)
    complements = db.relationship('Complements', back_populates="type_complement",  cascade="all, delete-orphan")


    def __init__(self, name, image = None):
        self.name = name
        self.image = image
    
    def __repr__(self):
        return  self.name
    
    #sererialize
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'complements': [complement.serialize() for complement in self.complements]
        }


def find_all_type_complements():
    type_complements = TypeComplements.query.all()
    serialize_type_complements = [type_complement.serialize() for type_complement in type_complements]
    return serialize_type_complements
    


    

def find_type_complement_by_id(id):
    return TypeComplements.query.get(id)


def find_type_complement_by_name(name):
    return TypeComplements.query.filter_by(name=name).first()


def create_type_complement(type_complement):
    try :
        db.session.add(type_complement)
        db.session.commit()
        return type_complement.serialize()
    except Exception as e:
        print(e)
        return False
    


def update_type_complement(id, type_complement):
    try :
        type_complement_to_update = find_type_complement_by_id(id)
        type_complement_to_update.name = type_complement.name
        type_complement_to_update.image = type_complement.image
        db.session.commit()
        return type_complement_to_update
    except:
        return False


def delete_type_complement(id):
    type_complement_to_delete = find_type_complement_by_id(id)
    db.session.delete(type_complement_to_delete)
    db.session.commit()
    return True


def delete_all_type_complements():
    db.session.query(TypeComplements).delete()
    db.session.commit()
    return True
        