from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import json

from user.models import User

user = Blueprint('user', __name__)

@user.route('/user', methods=('GET', 'POST'))
def register():
    return json.dumps({"greeting": "hi"})
