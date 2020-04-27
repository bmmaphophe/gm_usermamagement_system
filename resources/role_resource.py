from flask_restful import Resource, reqparse
from models.role_model import RoleModel
from flask import jsonify

class RoleManagement(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('rolename',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    def post(self):
        data = RoleManagement.parser.parse_args()

        if RoleModel.find_by_rolename(data['rolename']):
            return {"message": "A Role with the rolename already exists"}, 400

        role = RoleModel(data['rolename'], data['description'])
        role.save_role()

        return {"message": "Role created successfully."}, 201

class Roles(Resource):

    def get(self):
        role = RoleModel.find_all()
        if not role:
            return {'message':'Ckeck if Roles were created'}, 404
        return {'roles':[x.json() for x in RoleModel.find_all()]}
    
    # def gat(self,appname):
    #     pass

    # def get(self,id):
    #     pass