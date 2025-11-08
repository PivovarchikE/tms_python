from flask import Flask

from app.config import APP_CONFIG
from app.db.pg import close_connection

from .auth.views import auth_bp
from .survey.views import survey_bp


def create_app():
    app = Flask(__name__)

    app.secret_key = APP_CONFIG.get('secret_key')

    from app.db.commands import initialize_commands
    initialize_commands(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(survey_bp)

    app.teardown_appcontext(close_connection)
    return app
