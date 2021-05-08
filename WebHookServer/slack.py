from __future__ import print_function
import sys
import os
import requests
import json

# hide the slack webhook url
sys.path.append(os.path.join(os.path.dirname(__file__), "config"))
from slack_config import webhook_url

def post_slack(header, message, raw_event):
    slack_data = {'text': header + message}
    print(json.dumps(slack_data))

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


def post_slack_new(header, message, raw_event):
    attachments = {}
    if 'resolved' in raw_event['details']['Assurance Issue Status']:
        attachments['color'] = "good"
    elif 'active' in raw_event['details']['Assurance Issue Status']:
        attachments['color'] = "danger"
    else:
        attachments['color'] = "warning"
    attachments['fallback'] = header + message
    attachments['fields'] = {}
    fields = [{'title': raw_event['details']['Assurance Issue Details'], 'value': header + message, 'short': False}]
    attachments['fields'] = fields
    attachments['mrkdwn_in'] = ['value', 'fallback']
    data = {'attachments': [attachments] }
    print("data:\n")
    print(json.dumps(data))
    print("data slut\n")


    response = requests.post(
        webhook_url, data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
