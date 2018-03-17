from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import json

from object.models import Object

object_app = Blueprint('object', __name__)

@object_app.route('/object', methods=('GET', 'POST'))
def register():
    return json.dumps({"greeting": "hi"})
