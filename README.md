# Screenbot

This is a python bot which takes a screenshot of your main screen and sends it to a channel in slack
This was tested with python 3.7.3 on windows 10
## installing
Make sure the environment variable is a **system variable** (for windows) as variable `SLACK_BOT_TOKEN`, also the channel can be set as `SLACK_CHANNEL`.
If you have difficulties setting environment variables, follow [this article](https://www.computerhope.com/issues/ch000549.htm)

```
pip install -r requirements.txt
```

or if you don't have python installed, just use the binary from a release

## Usage
```
python screenbot.py
```
or
```
screenbot.exe
```

If you want to save the slack token and channel, run the script/executable in administrator mode. This is because it needs access to set the token and channel as environment variables.

This bot posts a picture when pressing the 'print screen' button and exits when 'escape' is pressed.