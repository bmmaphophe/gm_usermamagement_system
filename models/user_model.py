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
    username = db.Column(db.String(100),nullable =False,unique=True)
    password  = db.Column(db.String(100),nullable =False,)
    surname = db.Column(db.String(100))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    roles  = db.relationship('RoleModel', secondary=user_role_apptype_mapper, backref=db.backref('tbl_user',lazy='dynamic'))
    apps  = db.relationship('ApptypeModel', secondary=user_role_apptype_mapper, backref=db.backref('tbl_user',lazy='dynamic'))

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



