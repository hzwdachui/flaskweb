# encoding=utf-8
from flask import request, Blueprint, render_template, redirect, url_for, jsonify, current_app as app
from flask_login import login_required, current_user
from app import db, BASE_DIR
from demo.model.models import Todo, TodoItem
from demo.service.service import demoApiService

import os
modname = "debug"
bp = Blueprint(modname, modname, url_prefix="/debug",
               static_url_path="/static",
               static_folder=os.path.join(BASE_DIR, "./static"),
               template_folder=os.path.join(BASE_DIR, "./templates"))


@bp.route('/')
def index():
    return render_template('debug.html')

@bp.route('/api/v1/demo')
def demoApi():
    ret = demoApiService()
    return ret 
