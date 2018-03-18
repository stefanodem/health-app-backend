from application import db
from sqlalchemy import func
from entity.models import Entity
from like.models import Like


class Object(Entity):
    """
    A table for storing objects.
    An object my have a variety of object_types:
    - post
    - reply
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
        like_count = Like.query.filter_by(object_id=self.id).count()
        liked = Like.query.filter_by(user_id=self.owner_guid, object_id=self.id).scalar() is not None

        return {
            'postId': self.id,
            'user': {
                'uid': self.owner_guid,
            },
            'createdAt': self.created_at,
            'lastUpdated': self.updated_at,
            'body': self.body,
            'likeCount': like_count,
            'liked': liked,
        }
