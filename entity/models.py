from application import db
from flask import Blueprint
from utils.common import utc_now_ts as now

entity = Blueprint('entity', __name__)

class Entity(db.Model):
    """
    A table for storing base entities.
    The Entity class serves as a base class
    for users, objects, circles, and channels.

    """
    __tablename__ = 'entity'

    guid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)
    # reference to the object subtype, e.g. post
    # subtype = db.Column(db.String(30))
    owner_guid = db.Column(db.Integer)  # Column(Integer, ForeignKey('restaurant.id'))
    circle_guid = db.Column(db.Integer)  # Column(Integer, ForeignKey('restaurant.id'))
    # container_guid = db.Column(db.Integer)
    # access_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=now())
    updated_at = db.Column(db.DateTime, default=now())

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'entity'
    }

    def __repr__(self):
        return '<Entity {}>'.format(self.type)
