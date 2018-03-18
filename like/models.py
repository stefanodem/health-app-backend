from application import db
from flask import Blueprint

like_app = Blueprint('like', __name__)


class Like(db.Model):
    """
    A table for storing the likes.

    """

    __tablename__ = 'like'

    # composite key ensure that the combination of user and object id is unique
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    object_id = db.Column(db.Integer, db.ForeignKey('object.id'), primary_key=True)

    def __repr__(self):
        return '<Like {}>'.format(self.user_id)
