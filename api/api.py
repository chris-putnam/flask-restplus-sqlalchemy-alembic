try:
    from flask_restplus import Api
except ImportError:
    import flask.scaffold
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
    from flask_restplus import Api
import settings

SERVICE_NAME = settings.APP_NAME

api = Api(version='1.0', title=SERVICE_NAME, description='Test API')

ns = api.namespace(SERVICE_NAME, description='config service of ETP')
