from flask_restplus import fields
from api import api

role_details = api.model('role_details', {
    'name': fields.String(required=True, nullable=False, description='Role name'),
})
