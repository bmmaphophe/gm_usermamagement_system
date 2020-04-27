from db import db
class RoleModel(db.Model):
    __tablename__ = 'tbl_role'
    
    id = db.Column(db.Integer,primary_key =True) 
    rolename = db.Column(db.String(80))
    description = db.Column(db.String(80))

    def __init__(self,rolename,description):
        self.rolename = rolename
        self.description = description
                                                                                                                                                                                                                                                                                                                
    def save_role(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            "id": self.id,
            "rolename": self.rolename,
            "description": self.description
        }

    @classmethod
    def find_by_rolename(cls, rolename):
        return cls.query.filter_by(rolename=rolename).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()