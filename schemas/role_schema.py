from ma import ma
#from marshmallow_sqlalchemy import ModelSchema
from models.role_model import RoleModel


class RoleSchema(ma.ModelSchema):
    class Meta:
        model = RoleModel
        dump_only = ("id",)