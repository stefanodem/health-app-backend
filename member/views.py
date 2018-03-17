from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import json

from member.models import Member

member_app = Blueprint('member', __name__)

@member_app.route('/member', methods=('GET', 'POST'))
def register():
    return json.dumps({"greeting": "hi"})
