from db import db
from models.apptype_model import ApptypeModel
from models.role_model import RoleModel


user_role_apptype_mapper = db.Table("tbl_user_role_apptype_map",
    db.Column('user_id', db.Integer,db.ForeignKey('tbl_user.id')),
    db.Column('role_id', db.Integer,db.ForeignKey('tbl_role.id')),
    db.Column('apptype_id',db.Integer,db.ForeignKey('tbl_apptype.id'))
)

class UserModel(db.Model):
    __tablename__ = 'tbl_user'

    id = db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(80))
    password  = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    roles  = db.relationship('roleModel', secondary=user_role_apptype_mapper, backref=db.backref('roles',lazy='dynamic'))
    apps  = db.relationship('apptypeModel', secondary=user_role_apptype_mapper, backref=db.backref('apps',lazy='dynamic'))

    def __init__(self, username,password,surname,name,email):
       self.username = username
       self.password = password
       self.surname = surname
       self.name  = name
       self.email = email


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

