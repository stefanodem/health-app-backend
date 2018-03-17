from application import db
from entity.models import Entity


class Circle(Entity):
    __tablename__ = 'circle'

    id = db.Column(db.Integer, db.ForeignKey('entity.guid'), primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(260))

    __mapper_args__ = {
            'polymorphic_identity': 'circle',
    }

    def __repr__(self):
        return '<Circle {}>'.format(self.name)

    @property
    def serialize(self):
        return {
            'circleId': self.id,
            'name': self.name,
            'description': self.description,
            'lastUpdated': self.updated_at,
        }
