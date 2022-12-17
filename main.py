import flask
import requests
import json
import get_token
import get_workflow
import set_sales

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
import schedule

from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

token = ""

@app.route('/', methods=['GET'])
def home():
    username = request.args.get('username')
    password = request.args.get('password')
    application_id = request.args.get('application_id')
    application_custom_text1 = request.args.get('application_custom_text1')
    application_stage = request.args.get('application_stage')


    return {'application_id':application_id, 'application_custom_text1':application_custom_text1, 'application_stage':application_stage}

if __name__ == '__main__':
    # service.py executed as script

    app.run()

    scheduler = BlockingScheduler()
    scheduler.add_job(get_token.func, 'interval', days=1)
    scheduler.start()

    
    
