import time
from datetime import datetime, date, timedelta
from config import get_env

translate = {
    'chi': '你好',
    'ch': '你好',
    'en': 'Hello',
    'es': 'Hola',
    'jp': 'こんにちは-',
    'ko': '안녕하세요',
    'el': 'Χαίρετε',
    'fr': 'Bonjour',
    'de': 'Hallo',
    'lt': 'Sveiki',
    'ru': 'Здравствуйте'
}

class Actions:
    def __init__(self, slackhelper, user_info=None):
        self.user_info = user_info
        self.slackhelper = slackhelper

    def notify_channel(self):
        print("Worker is running")
        while True:
            print(f'Hello, message going to {self.slackhelper.slack_channel}')
            #self.slackhelper.post_message_to_channel('hi from hibot')
            time.sleep(600)

    def say_hi(self, lang='en'):
        message = f"{translate.get(lang, 'Hello')} {self.user_info['user']['profile']['display_name']}"
        recipient = self.user_info['user']['id']
        self.slackhelper.post_message(message, recipient)

    def say_hi_all(self, lang='en'):
        self.slackhelper.post_message_to_channel(f'{translate.get(lang, "Hello")} everyone!')

    def help(self):
        message=f"Available languages are "
        message = message + ','.join(translate.keys())
        recipient = self.user_info['user']['id']
        self.slackhelper.post_message(message, recipient)
