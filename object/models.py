from application import db
from sqlalchemy import func

from entity.models import Entity
from like.models import Like
from user.models import User


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
    parent_id = db.Column(db.Integer)
    body = db.Column(db.String(260))
    like_count = db.Column(db.Integer, default=0)
    visit_count = db.Column(db.Integer, default=0)
    reply_count = db.Column(db.Integer, default=0)
    enabled = db.Column(db.Boolean, default=True)

    __mapper_args__ = {
            'polymorphic_identity': 'object',
    }

    def __repr__(self):
        return '<Object {}>'.format(self.id)

    @property
    def serialize_post(self):
        like_count = Like.query.filter_by(object_id=self.id).count()
        liked = Like.query.filter_by(user_id=self.owner_guid, object_id=self.id).scalar() is not None
        user = User.query.filter_by(id=self.owner_guid).first()
        reply_count = Object.query.filter_by(parent_id=self.id).count()

        return {
            'postId': self.id,
            'user': {
                'uid': self.owner_guid,
                'name': user.username,
                'avatar': 'http://profile.actionsprout.com/default.jpeg',
            },
            'createdAt': self.created_at,
            'lastUpdated': self.updated_at,
            'body': self.body,
            'likeCount': like_count,
            'liked': liked,
            'replyCount': reply_count,
        }

    @property
    def serialize_reply(self):
        user = User.query.filter_by(id=self.owner_guid).first()

        return {
            'replyId': self.id,
            'user': {
                'uid': self.owner_guid,
                'name': user.username,
                'avatar': 'http://profile.actionsprout.com/default.jpeg',
            },
            'createdAt': self.created_at,
            'lastUpdated': self.updated_at,
            'body': self.body,
        }
