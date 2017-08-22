from app import app
from app import db
from flask import render_template, request, jsonify
from app import celery_obj


@app.route('/', methods=['GET','POST'])
def index():
    return "it works"


