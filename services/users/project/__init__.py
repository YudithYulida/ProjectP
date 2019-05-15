# services/users/project/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
# instanciado la db
db = SQLAlchemy()
toolbar = DebugToolbarExtension()


# nuevo
def create_app(script_info=None):
    # instanciando app
    app = Flask(__name__)

    # habilitando CORS
    CORS(app)
    # estableciendo configuración
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # estableciendo extextensiones
    db.init_app(app)
    toolbar.init_app(app)

    # registrando blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # contexto shell para flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
