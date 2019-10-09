# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:06:58 2018

@author: Rajman
"""

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
