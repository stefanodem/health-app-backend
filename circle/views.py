from flask import Blueprint, jsonify, request, session, url_for, abort
import json
from application import db

from circle.models import Circle
from object.models import Object
from member.models import Member

circle_app = Blueprint('circle', __name__)


@circle_app.route('/circles', methods=['POST'])
def create_circle():
    if request.is_json and request.method == 'POST':
        response = request.get_json()
        new_circle = Circle(name=response['name'], description=response['description'])
        db.session.add(new_circle)
        db.session.commit()
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    else:
        abort(400)


@circle_app.route('/circles/<int:circle_id>', methods=['DELETE'])
def delete_circle(circle_id):
    if request.method == 'DELETE':
        circle = Circle.query.get(circle_id)
        db.session.delete(circle)
        db.session.commit()
        return json.dumps({'success': True}), 204, {'ContentType': 'application/json'}
    else:
        abort(400)


@circle_app.route('/circles/<int:circle_id>/posts', methods=['GET', 'POST'])
def get_circle_posts(circle_id):
    if circle_id:
        posts = Object.query.filter_by(circle_guid=circle_id, object_type='post').all()
        if posts:
            return jsonify(posts=[post.serialize_post for post in posts])
        else:
            abort(404)
    else:
        abort(404)


@circle_app.route('/circles/<int:circle_id>/members', methods=['GET', 'POST'])
def get_circle_members(circle_id):
    if circle_id:
        members = Member.query.filter_by(circle_id=circle_id).all()
        if members:
            member_ids = [member.user_id for member in members]
            member_profiles = User.query.filter(User.id.in_(member_ids)).all()
            return jsonify(members=[member.serialize_member for member in member_profiles])
        else:
            abort(404)
    else:
        abort(404)
