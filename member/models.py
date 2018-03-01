from application import db


class Member(db.Model):
    """
    A table for storing the membership of a user to a circle.

    """

    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True)
    user_guid = db.Column(db.Integer, db.ForeignKey('user.id'))
    circle_guid = db.Column(db.Integer, db.ForeignKey('circle.id'))
    channel_guid = db.Column(db.Integer, db.ForeignKey('channel.id'))

    def __repr__(self):
        return '<Member {}>'.format(self.user_guid)
