import flask
import requests
import json
import get_token
import get_workflow
import set_sales
import synchronize
import process_data
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
import schedule

from flask import request
import os
import logging
app = flask.Flask(__name__)
app.config["DEBUG"] = True

LOG_NAME = 'webhook.log'

@app.route('/webhook', methods=['POST'])
def home():
    with open(LOG_NAME,'w'):
        pass
    logging.basicConfig(filename=LOG_NAME, level=logging.INFO)
    data = request.get_json()
    print(data)
    try:
        workflow = get_workflow.main()
        print(workflow)

        ticketData = process_data.main(data)
        print(ticketData)

        synchronize.main(data, ticketData, workflow)

    except Exception as e:
        logging.info(e)
        print(e)


    return ""

if __name__ == '__main__':
    # service.py executed as script

    app.run('0.0.0.0', port=3000)

    scheduler = BlockingScheduler()
    scheduler.add_job(get_token.func, 'interval', days=1)
    scheduler.start()

    
    
