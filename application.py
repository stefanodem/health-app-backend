from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
with app.app_context():
    from entity.models import Entity
    from user.models import User
    from object.models import Object
    from circle.models import Circle
    from channel.models import Channel
    db.create_all()

migrate = Migrate(app, db)

from entity.models import entity
app.register_blueprint(entity)

from user.views import user
app.register_blueprint(user)

from object.views import object
app.register_blueprint(object)

from circle.views import circle
app.register_blueprint(circle)

from channel.views import channel
app.register_blueprint(channel)

def create_app():
    return app

# from application import routes, models

# db = SQLAlchemy()
#
#
# def create_app(**config_overrides):
#     app = Flask(__name__)
#     # loading configuration for this instance
#     app.config.from_object(Config)
#
#     # overriding settings if any config_override is passed as param (e.g. testing)
#     app.config.update(config_overrides)
#
#     # db = SQLAlchemy(app)
#     db.init_app(app)
#
#     # with app.test_request_context():
#     #     from user.models import User
#     #     db.create_all()
#
#     with app.app_context():
#         db.init_app(app)
#
#     db.create_all()
#
#     # migrate = Migrate(app, db)
#
#     from app import routes, models
#
#     # registering blueprint
#     from user.views import user_app
#     app.register_blueprint(user_app)
#
#     from object.views import posts_app
#     app.register_blueprint(posts_app)
#
#     return app
