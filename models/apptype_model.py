from db import db

class ApptypeModel(db.Model):
    __tablename__ = 'tbl_apptype'
    id = db.Column(db.Integer,primary_key =True)
    appname = db.Column(db.String(80))
    description = db.Column(db.String(80))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_appname(cls,appname):
        return cls.query.filter_by(appname = appname).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        
