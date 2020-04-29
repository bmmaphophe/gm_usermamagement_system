from ma import ma
#from marshmallow_sqlalchemy import ModelSchema
from models.user_model import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)