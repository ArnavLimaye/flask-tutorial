import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db

bp = Blueprint('chat', __name__, url_prefix='/chat')


def process_input(user_input):
    print("User Input : ", user_input)
    return user_input[::-1]


@bp.route('/', methods=('GET', 'POST'))
def chat():
    bot_reply = "BOT : Please enter your question to make me talk. Enter quit to mute me."
    if request.method == 'POST':
        error = None
        user_input = request.form['user_input']
        bot_reply = process_input(user_input)
        if(error != None):
            flash(error)
    return render_template('chat/chat_room.html', bot_reply=bot_reply)
