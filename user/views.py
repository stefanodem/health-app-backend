from flask import Blueprint, jsonify, request, session, url_for, abort
import json
from utils import error

from user.models import User
from circle.models import Circle
from object.models import Object
from member.models import Member

user_app = Blueprint('user', __name__)


@user_app.route('/user/<int:user_id>', methods=('GET', 'POST'))
def get_user(user_id):
    if user_id:
        user = User.query.filter_by(id=user_id).one()
        if user:
            return jsonify(user=user.get_info)
        else:
            abort(404)
    else:
        abort(404)


@user_app.route('/user/circles/<int:user_id>', methods=('GET', 'POST'))
def get_user_circles(user_id):
    if user_id:
        circles = Circle.query.filter_by(owner_guid=user_id).all()
        if circles:
            return jsonify(circles=[circle.serialize for circle in circles])
        else:
            abort(404)
    else:
        abort(404)


@user_app.route('/user/posts/<int:user_id>', methods=('GET', 'POST'))
def get_user_posts(user_id):
    if user_id:
        posts = Object.query.filter_by(owner_guid=user_id, object_type='post').all()
        if posts:
            return jsonify(posts=[post.serialize_post for post in posts])
        else:
            abort(404)
    else:
        abort(404)


@user_app.route('/user/members/<int:circle_id>', methods=('GET', 'POST'))
def get_circle_members(circle_id):
    if circle_id:
        members = Member.query.filter_by(circle_id=circle_id).all()
        if members:
            member_ids = [member.user_id for member in members]
            member_profiles = User.query.filter(User.id.in_(member_ids)).all()
            return jsonify(members=[member.get_members for member in member_profiles])
        else:
            abort(404)
    else:
        abort(404)

