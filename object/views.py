from flask import Blueprint, jsonify, request, session, url_for, abort
from application import db
import json

from object.models import Object
from like.models import Like

object_app = Blueprint('object', __name__)


@object_app.route('/users/<int:user_id>/posts/<int:post_id>/like', methods=['POST', 'DELETE'])
def handle_like(user_id, post_id):
    if request.is_json and request.method == 'POST':
        post_like = Like(user_id=user_id, object_id=post_id)
        db.session.add(post_like)
        db.session.commit()
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    if request.is_json and request.method == 'DELETE':
        post_like = Like.query.filter_by(user_id=user_id, object_id=post_id).one()
        db.session.delete(post_like)
        db.session.commit()
        return json.dumps({'success': True}), 204, {'ContentType': 'application/json'}
    else:
        abort(400)


@object_app.route('/posts/<int:post_id>/replies', methods=['GET', 'POST'])
def handle_replies(post_id):
    if request.is_json and request.method == 'GET':
        replies = Object.query.filter_by(parent_id=post_id).all()
        if replies:
            return jsonify(replies=[reply.serialize_reply for reply in replies])
        else:
            abort(404)
    if request.is_json and request.method == 'POST':
        response = request.get_json()
        new_reply = Object(owner_guid=response['userId'],
                           circle_guid=response['circleId'],
                           type='object',
                           object_type='reply',
                           parent_id=post_id,
                           body=response['body'])
        db.session.add(new_reply)
        db.session.commit()
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    else:
        abort(404)

