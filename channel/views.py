from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import json

from channel.models import Channel

channel_app = Blueprint('channel', __name__)

@channel_app.route('/channel', methods=('GET', 'POST'))
def register():
    return json.dumps({"greeting": "hi"})
