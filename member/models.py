from application import db


class Member(db.Model):
    """
    A table for storing the membership of a user to a circle.

    """

    __tablename__ = 'member'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    circle_id = db.Column(db.Integer, db.ForeignKey('circle.id'))
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))

    def __repr__(self):
        return '<Member {}>'.format(self.user_guid)
