from flask_api import FlaskAPI
from flask import request, jsonify
from config.env import app_env
from app.utils.slackhelper import SlackHelper
from app.actions import Actions

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')

    @app.route('/hibot', methods=['POST'])
    def home():
        print(request.data)
        print(request.json)
        command_text = request.data.get('text')
        slack_uid = request.data.get('user_id')
        slackhelper = SlackHelper()
        slack_user_info = slackhelper.user_info(slack_uid)
        actions = Actions(slackhelper, slack_user_info)

        if command_text:
            command_text = command_text.split(' ')
            if command_text[0] == 'help':
                response_body = actions.help()
            elif command_text[0] == 'pingpong':
                response_body = actions.post_leaderboard()
            elif len(command_text) == 2 and command_text[1] == 'all':
                response_body = actions.say_hi_all(command_text[0])
            else:
                response_body = actions.say_hi(command_text[0])
        else:
            response_body = actions.say_hi()

        response = jsonify(response_body)
        response.status_code = 200

        return response

    return app
