from flask_restful import Resource
from flask import Request
from models.role_model import RoleModel
from flask import jsonify

from flask import request
from marshmallow import ValidationError

from schemas.role_schema import RoleSchema

role_schema = RoleSchema();
roles_list_schema = RoleSchema(many=True);

class RoleManagement(Resource):

    
    def post(self):
        try:
            role = role_schema.load(request.get_json())
        except ValidationError as err:
            return err.message,400
        if RoleModel.find_by_rolename(role.rolename):
            return {"message": "A Role with the rolename already exists"}, 400
        role.save_role()
        return {"message": "Role created successfully."}, 201


class Roles(Resource):
    @classmethod
    def get(cls):
        roles = RoleModel.find_all()
        if not roles:
            return {'message':'Ckeck if Roles were created'}, 404
        return roles_list_schema.dump(roles)


class Role(Resource):

    @classmethod
    def gat(cls,appname):
        pass

    @classmethod
    def get(cls,id):
        pass