from flask_restplus import Resource
from sqlalchemy.orm import joinedload
from api.api import api, ns
from database.model import *
from serializers import user_details, role_details


@ns.route('/')
class DefaultCollection(Resource):
    def get(self):
        return {'msg': 'Hi'}


@ns.route('/user')
class UserCollection(Resource):
    @api.marshal_with(user_details)
    def get(self):
        users = User.query.options(joinedload(
            User.role, innerjoin=True)).all()
        return users


@ns.route('/role')
class RoleCollection(Resource):
    @api.marshal_with(role_details)
    def get(self):
        roles = Role.query.all()
        return roles
