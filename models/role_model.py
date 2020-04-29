from db import db
class RoleModel(db.Model):
    __tablename__ = 'tbl_role'
    
    id = db.Column(db.Integer,primary_key =True) 
    rolename = db.Column(db.String(80),nullable =False,unique=True)
    description = db.Column(db.String(80),nullable =False)

                                                                                                                                                                                                                                                                                                         
    def save_role(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_rolename(cls, rolename):
        return cls.query.filter_by(rolename=rolename).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()