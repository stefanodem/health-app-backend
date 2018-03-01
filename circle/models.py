from application import db
from entity.models import Entity
from utils.common import utc_now_ts as now


class Circle(Entity):
    __tablename__ = 'circle'

    id = db.Column(db.Integer, db.ForeignKey('entity.guid'), primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(260))
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    __mapper_args__ = {
            'polymorphic_identity':'circle',
    }

    def __repr__(self):
        return '<Circle {}>'.format(self.name)
