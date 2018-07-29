from flask_restful import Resource, reqparse
from app import app, api

users = [{
    "id" : 1,
    "name" : "Matheus",
    "email" : "matheuscunhareis30@gmail.com",
    "password" : "matheus1234",
    "city" : "Uberlandia",
    "age" : 13,
    "phone" : "987456123"
}
]

class UserApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("name", type=str, location='json')
        self.reqparse.add_argument("email", type=str, location='json')
        self.reqparse.add_argument("password", type=str, location='json')
        self.reqparse.add_argument("city", type=str, location='json')
        self.reqparse.add_argument("age", type=int, location='json')
        self.reqparse.add_argument("phone", type=str, location='json')
        super(UserApi, self).__init__()

    def get(self, id):
        user = next(filter(lambda u: u['id'] == id, users))
        return {'user' : user}, 200

    def put(self, id):
        return {"message" : "Hi"}

    def delete(self, id):
        pass

class UserListApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("name", type=str, required=True, location='json')
        self.reqparse.add_argument("email", type=str, required=True, location='json')
        self.reqparse.add_argument("password", type=str, required=True, location='json')
        self.reqparse.add_argument("city", type=str, location='json')
        self.reqparse.add_argument("age", type=int, location='json')
        self.reqparse.add_argument("phone", type=str, location='json')
        super(UserListApi, self).__init__()

    def get(self):
        return {"users" : users}, 200

    def post(self):
        args = self.reqparse.parse_args()
        users.append(args)
        return {"message" : "sucess"}, 200

api.add_resource(UserApi, '/api/users/<int:id>', endpoint='user')
api.add_resource(UserListApi, '/api/users', endpoint='user_list')
