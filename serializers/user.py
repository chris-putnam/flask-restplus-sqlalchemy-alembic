from flask_restplus import fields
from api import api

from .role import role_details

user_details = api.model('user_details', {
    'id': fields.Integer(required=True, description='Id'),
    'username': fields.String(required=True, nullable=False, description='Username'),
    'email': fields.String(required=True, nullable=False, description='Email'),
    'role': role_details
})
