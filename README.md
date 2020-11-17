# Screenbot

This is a python bot which takes a screenshot of your main screen and sends it to a channel in slack
This was tested with python 3.7.3 on windows 10
## installing
Make sure the environment variable is a system variable (for windows) as variable `SLACK_BOT_TOKEN`.
If you have difficulties setting environment variables, follow [this article](https://www.computerhope.com/issues/ch000549.htm)
```
pip install -r requirements.txt
```

## Usage
```
python screenbot.py 'slacktoken' 'channel'
```