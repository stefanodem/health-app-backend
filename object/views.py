from flask import Blueprint, render_template, request, redirect, session, url_for, abort
from application import db
import json

from object.models import Object
from like.models import Like

object_app = Blueprint('object', __name__)


@object_app.route('/users/<int:user_id>/posts/<int:post_id>/like', methods=['POST'])
def add_like(user_id, post_id):
    if request.is_json and request.method == 'POST':
        liked_post = Like(user_id=user_id, object_id=post_id)
        db.session.add(liked_post)
        db.session.commit()
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    else:
        abort(400)
