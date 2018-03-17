from flask import Blueprint, jsonify, request, session, url_for, abort
import json

from circle.models import Circle
from object.models import Object
from member.models import Member

circle_app = Blueprint('circle', __name__)

@circle_app.route('/circles/<int:circle_id>/posts', methods=('GET', 'POST'))
def get_circle_posts(circle_id):
    if circle_id:
        posts = Object.query.filter_by(circle_guid=circle_id, object_type='post').all()
        if posts:
            return jsonify(posts=[post.serialize_post for post in posts])
        else:
            abort(404)
    else:
        abort(404)
