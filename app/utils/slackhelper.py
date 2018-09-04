from slackclient import SlackClient
from config import get_env

class SlackHelper:
    def __init__(self):
        self.slack_token = get_env('SLACK_TOKEN')
        self.slack_client = SlackClient(self.slack_token)
        self.slack_channel = get_env('SLACK_CHANNEL')
        self.botname = get_env('BOTNAME')

    def post_message(self, message, recipient):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=recipient,
            text=message,
            as_user=True
        )

    def post_message_to_channel(self, message):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            text=message,
            username=self.botname,
            parse='full',
            as_user=False
        )

    def user_info(self, user_id):
        return self.slack_client.api_call(
            "users.info",
            user=user_id,
            token=self.slack_token
        )
