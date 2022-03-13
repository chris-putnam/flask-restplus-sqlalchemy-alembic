from flask import Blueprint, Flask, request

from database import db, user

from api import endpoint

import settings

APP_NAME = settings.APP_NAME
app = Flask(APP_NAME)


def configure_app(flask_app):
    flask_app.config['PROPAGATE_EXCEPTIONS'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['SQLALCHEMY_ECHO'] = True


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='')
    endpoint.api.init_app(blueprint)
    endpoint.api.add_namespace(endpoint.ns)
    flask_app.register_blueprint(blueprint)

    with app.app_context():
        db.init_app(app)
        # db.create_all()

        # try:
        #     user1 = user.User(username='chris',
        #                       email='chris.putnam@swedenstreet.com')
        #     db.session.add(user1)
        #     db.session.commit()
        # except Exception as e:
        #     print(e)


def main():
    initialize_app(app)
    app.run(host='0.0.0.0', port=settings.FLASK_PORT,
            debug=settings.FLASK_DEBUG)


if __name__ == '__main__':
    main()

if __name__ != '__main__':
    initialize_app(app)
