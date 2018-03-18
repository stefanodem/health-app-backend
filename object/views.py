from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import json

from object.models import Object

object_app = Blueprint('object', __name__)

@object_app.route('/posts/<int:post_id>/replies', methods=['GET', 'POST'])
def get_post_replies():
    return json.dumps({"greeting": "hi"})
