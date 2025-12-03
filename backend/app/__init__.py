
from flask import Flask
# from app.api.auth import auth_blueprint
from .api.health_check import bp as health_check
# from app.db.users_db import create_table

def create_app():
    app = Flask(__name__)

    # create_table()

    # app.register_blueprint(auth_blueprint)
    app.register_blueprint(health_check, url_prefix="/api")

    return app

app = create_app()