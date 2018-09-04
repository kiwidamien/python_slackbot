import requests
from slackclient import SlackClient
from dotenv import load_dotenv
import sys
import os
from werkzeug.datastructures import MultiDict

user_id = sys.argv[1]
load_dotenv('.env')

print(os.environ['SLACK_TOKEN'])
params = MultiDict([('text', 'en'), ('user_id', user_id), ('token', os.environ['SLACK_TOKEN'])])

r = requests.post('https://hello-bot-damien.herokuapp.com/hibot', data=params)
print(r)
