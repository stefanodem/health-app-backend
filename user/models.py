from application import db
from entity.models import Entity
from utils.common import utc_now_ts as now


class User(Entity):
    """
    A table for storing user records.

    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, db.ForeignKey('entity.guid'), primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    language = db.Column(db.String(64), nullable=False)
    # session code
    code = db.Column(db.Integer)
    last_action = db.Column(db.DateTime, default=now())
    prev_last_action = db.Column(db.DateTime, default=now())
    last_login = db.Column(db.DateTime, default=now())
    prev_last_login = db.Column(db.DateTime, default=now())

    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }

    def __repr__(self):
        return '<User {}>'.format(self.username)
