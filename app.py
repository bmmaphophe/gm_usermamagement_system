from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
#from flask_jwt import JWT

from resources.user_resource import UserManagement, UserLogin
from security.security import authenticate , identity
from resources.role_resource import RoleManagement, Roles 
from resources.apptype_resource import AppManagement


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gmusermanagementsystem.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'gm' #app.config['JWT_SECRET_KEY']
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

#jwt = JWT(app, authenticate, identity)  # /auth
jwt = JWTManager(app)

# end points 
api.add_resource(UserManagement,'/api/user/register')
api.add_resource(RoleManagement,'/api/role/register')
api.add_resource(Roles,'/api/roles')
api.add_resource(AppManagement,'/api/app/register')

api.add_resource(UserLogin, '/api/auth')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=8181,debug=True)