from application import db
from entity.models import Entity


class Object(Entity):
    """
    A table for storing objects.
    An object my have a variety of subtypes:
    - post
    - etc.

    """
    __tablename__ = 'object'

    id = db.Column(db.Integer, db.ForeignKey('entity.guid'), primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.String(260))
    enabled = db.Column(db.Boolean)

    __mapper_args__ = {
            'polymorphic_identity':'object',
    }

    def __repr__(self):
        return '<Object {}>'.format(self.title)
