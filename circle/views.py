from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import json

from circle.models import Circle

circle = Blueprint('circle', __name__)

@circle.route('/circle', methods=('GET', 'POST'))
def register():
    return json.dumps({"greeting": "hi"})
