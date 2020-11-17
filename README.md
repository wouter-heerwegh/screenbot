# Screenbot

This is a python bot which takes a screenshot of your main screen and sends it to a channel in slack
This was tested with python 3.7.3 on windows 10
## installing
Make sure the environment variable is a system variable (for windows) as variable `SLACK_BOT_TOKEN`.
If you have difficulties setting environment variables, follow [this article](https://www.computerhope.com/issues/ch000549.htm)
```
pip install -r requirements.txt
```
or just use the binary from a release

## Usage
```
python screenbot.py 'slack_token' 'channel'
```
or:
```
screenbot.exe 'slack_token' 'channel'
```

if you have the slack_token set as an environment variable you dont have to give the slack token:
```
python screenbot.py 'channel'
```