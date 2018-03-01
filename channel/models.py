from application import db
from entity.models import Entity
from utils.common import utc_now_ts as now


class Channel(Entity):
    """
    A table for storing communication channels.

    """
    __tablename__ = 'channel'

    id = db.Column(db.Integer, db.ForeignKey('entity.guid'), primary_key=True)
    name = db.Column(db.String(60))
    public = db.Column(db.Boolean)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    __mapper_args__ = {
            'polymorphic_identity':'channel',
    }

    def __repr__(self):
        return '<Channel {}>'.format(self.name)
