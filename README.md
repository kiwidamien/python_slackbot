# Making a Slackbot in Python

We will be making a slackbot called `HelloBot`, which will implement one command `/hibot [language]`, where `[language]` is a two-letter code for the language of choice. If not language is given, it will default to English.

The name of the bot is controlled in the `.env` file.

We need to setup in two places:
* Slack
* Heroku

## Setup on Slack
1. Clone this repo
2. Go to https://api.slack.com/apps/new to create a new app. Fill in the app name with the name of your bot, and the `Development Slack Workspace` as the name of the workspace you want to use your bot in.
3. Select *Bot Users* and "Add a Bot User"
  ![Adding a bot user](images/tutorial/add_a_bot.png)
  We will be calling our bot user `HelloBot`.
4. Now click `Install App` from the left menu (under Settings), then click `Install App to Workspace`
  ![Installing the app](images/tutorial/install_app.png)

  You will be asked to authorize your bot. Do it!
5.  Copy the slack token and OAuth into your `.env` file:
```bash
FLASK_APP="hellobot.py"
APP_ENV="development" # leave as development
SLACK_CHANNEL=......  # id of the channel the bot posts in; will look something like "CBPK9CPCZ"
SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # some random characters
OAuth=xoxp-........ # your OAuth will start with xoxp-
SLACK_TOKEN=xoxb-...# your SLACK_TOKEN will start with xoxb-
BOTNAME='HelloBot'  # name of the bot
```
  Don't include the comment hashes (this will be important when deploying to Heroku)

### Testing
Once you have done all of this, you can use python to test your configuration. You will need to find your user id. Go to https://summer-sf18-metis.slack.com/stats#members and click "Edit Columns". Select "User id" and copy-and-paste your user id:
  ![Getting user id](images/tutorial/get_user_id.png)

* Run the app in one terminal window:
```python
python hellobot.py
```
* In a separate terminal, load python and run the following script:
```python
python test/send_test_message.py <USERID>
```
where <USERID> is your user id found above. It is a string like `UBDHZ54EQ`, NOT your display name!

If the test is successful, you should receive a message from HelloBot saying "Hello <your display name>"

## Setup Heroku
1. Install heroku: `brew install heroku/brew/heroku`
2. Create a heroku app with `heroku create <appname>`. Replace <appname> with an application name of your choice. Note that this name cannot be used by any other app. I will call my `hello-bot-damien`, but you will need another name for yours.
3. Setup Heroku environment variables with `./setup_env.sh`
4. Run `git push heroku master`

## Going further / customizing
