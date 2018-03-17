from application import db
from entity.models import Entity


class Object(Entity):
    """
    A table for storing objects.
    An object my have a variety of object_types:
    - post
    - etc.

    """
    __tablename__ = 'object'

    id = db.Column(db.Integer, db.ForeignKey('entity.guid'), primary_key=True)
    # Object types: post, reply
    object_type = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(60))
    body = db.Column(db.String(260))
    like_count = db.Column(db.Integer)
    visit_count = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)
    enabled = db.Column(db.Boolean)

    __mapper_args__ = {
            'polymorphic_identity': 'object',
    }

    def __repr__(self):
        return '<Object {}>'.format(self.owner_guid)

    # TODO: find way to set liked to True or False
    @property
    def serialize_post(self):
        return {
            'postId': self.id,
            'user': {
                'uid': self.owner_guid,
            },
            'createdAt': self.created_at,
            'lastUpdated': self.updated_at,
            'body': self.body,
            'likeCount': self.like_count,
            'liked': True,
        }
