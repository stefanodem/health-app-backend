from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import json

from channel.models import Channel

channel = Blueprint('channel', __name__)

@channel.route('/channel', methods=('GET', 'POST'))
def register():
    return json.dumps({"greeting": "hi"})
