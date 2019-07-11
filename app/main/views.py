from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from flask_login import login_required, current_user
from .. import db
from datetime import datetime
from time import time, sleep
from ..email import send_subscriptions, send_blogs
import markdown2


@main.route('/')
def index():
    return render_template("index.html")

@main.route('/subscribed')
def subscribed():
    
    sleep(5)
    # return redirect(url_for('main.index'))

    return render_template('subscribed.html', title = 'Subscribed!')