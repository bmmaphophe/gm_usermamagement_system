from collections import Counter

from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token

from models.user_model import UserModel, UserRoleMapper
from schemas.user_schema import UserSchema

user_schema = UserSchema()
users_schema = UserSchema()


class UserManagement(Resource):

    def post(self):
        roles = []
        user_data = request.get_json()
        if UserModel.find_by_username(user_data["username"]):
            return {"message": "A user with that username already exists"}, 400

        roles_list = Counter(user_data['roles'])

        for _id in roles_list:
            roles.append(UserRoleMapper(role_id=_id))

        user = UserModel(roles=roles)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

class Users(Resource):
    def get(self):
        users = UserModel.find_all()
        if not users:
            return {'message': 'Ckeck if Users were created'}, 404
        return users_schema.dump(users)

class User(Resource):
    
    def gat(self, appname):
        pass

    def get(self, id):
        pass

class UserLogin(Resource):

    @classmethod
    def post(cls):
        try:
            user = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.message, 400
        
        user = UserModel.find_by_username(user.username)
        if user and safe_str_cmp(user.password, user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return{
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 200
        return {"message": "Invalid credentials"}, 401