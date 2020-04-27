from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token
from models.user_model import UserModel

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
_user_parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
_user_parser.add_argument('name',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
_user_parser.add_argument('surname',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )

_user_parser.add_argument('email',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )

class UserManagement(Resource):

    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201


    def get(self):
        pass
    
    def gat(self,appname):
        pass

    def get(self, id):
        pass


class UserLogin(Resource):

    @classmethod
    def post(cls):
        data = _user_parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user and safe_str_cmp(user.password,data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return{
                "access_token":access_token,
                "refresh_token":refresh_token
            }, 200
        return {"message":"Invalid credentials"},401