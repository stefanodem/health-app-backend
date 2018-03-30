from flask import Blueprint, jsonify, request, session, url_for, abort
from application import db
import json

from object.models import Object
from like.models import Like

object_app = Blueprint('object', __name__)


@object_app.route('/users/<int:user_id>/circles/<int:circle_id>/posts', methods=['GET', 'POST'])
def handle_posts(user_id, circle_id):
    if request.is_json and request.method == 'POST':
        response = request.get_json()
        new_post = Object(owner_guid=user_id,
                          circle_guid=circle_id,
                          type='object',
                          object_type='post',
                          body=response['body'])
        db.session.add(new_post)
        db.session.commit()
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    if request.method == 'GET':
        posts = Object.query.filter_by(circle_guid=circle_id, object_type='post').all()
        return jsonify(posts=[post.serialize_post(user_id) for post in posts])
    else:
        abort(400)


@object_app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Object.query.filter_by(id=post_id).one()
    db.session.delete(post)
    db.session.commit()
    return json.dumps({'success': True}), 204, {'ContentType': 'application/json'}



@object_app.route('/users/<int:user_id>/posts/<int:post_id>/like', methods=['POST', 'DELETE'])
def handle_like(user_id, post_id):
    if request.method == 'POST':
        post_like = Like(user_id=user_id, object_id=post_id)
        db.session.add(post_like)
        db.session.commit()
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    if request.method == 'DELETE':
        post_like = Like.query.filter_by(user_id=user_id, object_id=post_id).one()
        db.session.delete(post_like)
        db.session.commit()
        return json.dumps({'success': True}), 204, {'ContentType': 'application/json'}
    else:
        abort(400)


@object_app.route('/posts/<int:post_id>/replies', methods=['GET', 'POST'])
def handle_replies(post_id):
    if request.method == 'GET':
        replies = Object.query.filter_by(parent_id=post_id).all()
        return jsonify(replies=[reply.serialize_reply for reply in replies])
    if request.is_json and request.method == 'POST':
        response = request.get_json()
        new_reply = Object(owner_guid=response['userId'],
                           type='object',
                           object_type='reply',
                           parent_id=post_id,
                           body=response['body'])
        db.session.add(new_reply)
        db.session.commit()
        replies = Object.query.filter_by(parent_id=post_id).all()
        return jsonify(replies=[reply.serialize_reply for reply in replies])
    else:
        abort(404)

