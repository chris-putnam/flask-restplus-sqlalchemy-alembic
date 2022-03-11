from flask_restplus import fields
from api import api

user_details = api.model('user_details', {
    'username': fields.String(required=True, nullable=False, description='Username'),
    'email': fields.String(required=True, nullable=False, description='Email'),
})
