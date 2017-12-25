import logging.config

from flask import Flask, Blueprint
from app import settings
from app.api.test.endpoints.tests import ns as tests_namespace
from app.api.restplus import api

app = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME + ':' + settings.FLASK_SERVER_PORT
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(tests_namespace)
    # add more namespaces here
    flask_app.register_blueprint(blueprint)


def main():
    initialize_app(app)
    log.info('===== Starting development server at http://{}/api/ ====='.format(settings.FLASK_SERVER_NAME))
    app.run(debug=settings.FLASK_DEBUG, host=settings.FLASK_SERVER_NAME)

if __name__ == "__main__":
    main()
