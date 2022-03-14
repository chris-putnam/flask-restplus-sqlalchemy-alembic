from flask_restplus import fields
from api import api

role_details = api.model('role_details', {
    'id': fields.Integer(required=True, description='Id'),
    'name': fields.String(required=True, nullable=False, description='Role name'),
})
