from __future__ import print_function
import sys
import os
import requests
import json

# hide the slack webhook url
sys.path.append(os.path.join(os.path.dirname(__file__), "config"))
from slack_config import webhook_url

def post_slack(header,message):
    # Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook
    slack_data = {'text': header + message}

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )