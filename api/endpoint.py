from flask_restplus import Resource
from api.api import api, ns
from database.user import User
from serializers import user_details


@ns.route('/')
class DefaultCollection(Resource):
    @api.marshal_with(user_details)
    def get(self):
        users = User.query.all()
        return users
