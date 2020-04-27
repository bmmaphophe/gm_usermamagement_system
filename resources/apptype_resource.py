from flask_restful import Resource, reqparse
from models.apptype_model import ApptypeModel

class AppManagement(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('appname',
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
        data = AppManagement.parser.parse_args()

        if ApptypeModel.find_by_appname(data['appname']):
            return {"message": "A App Name with the appname already exists"}, 400

        app = ApptypeModel(data['appname'], data['description'])
        app.save_to_db()

        return {"message": "Appname created successfully."}, 201

        
    def get(self):
        pass
    
    def gat(self,appname):
        pass

    def get(self, id):
        pass