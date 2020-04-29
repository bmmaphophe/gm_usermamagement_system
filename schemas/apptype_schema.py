from ma import ma
#from marshmallow_sqlalchemy import ModelSchema
from models.apptype_model import ApptypeModel


class AppTypeSchema(ma.ModelSchema):
    class Meta:
        model = ApptypeModel
        dump_only = ("id",)