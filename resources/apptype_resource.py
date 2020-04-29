from flask_restful import Resource

from flask import request
from marshmallow import ValidationError

from models.apptype_model import ApptypeModel
from schemas.apptype_schema import AppTypeSchema

apptype_schema = AppTypeSchema()
apptypes_schema = AppTypeSchema(many=True)

class AppManagement(Resource):

    @classmethod
    def post(cls):
        try:
            app = apptype_schema.load(request.get_json())
        except ValidationError as err:
            return err.message,400
        if ApptypeModel.find_by_appname(app.appname):
            return {"message": "A App Name with the appname already exists"}, 400
        app.save_to_db()
        return {"message": "Appname created successfully."}, 201

class Apptypes(Resource):       
    def get(self):
        apptypes = ApptypeModel.find_all()
        if not apptypes:
            return {'message':'Ckeck if AppTypes were created'}, 404
        return apptypes_schema.dump(apptypes)

        
class AppType(Resource):        
    def gat(self,appname):
        pass

    def get(self, id):
        pass