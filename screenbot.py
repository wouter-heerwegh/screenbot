from pynput import keyboard
import slack, os, pyautogui, sys

def on_press(key):
    if key == keyboard.Key.print_screen:
        print('posting')
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('screen.png')
        try:
            client.files_upload(channels=channel,
                file='screen.png',
                title='Test upload')
        except slack.errors.SlackApiError:
            e = sys.exc_info()
            print("Failed to upload to slack, maybe the token or channel are not correct?")
            print("Error traceback: ", e)

    elif key == keyboard.Key.esc:
        exit()

if __name__ == "__main__":
    slack_token = ''
    channel = ''

    if len(sys.argv) == 1 :
        print("Not enough arguments\nUsage: python screenbot.py 'slacktoken' 'channel'")
        exit()
    elif len(sys.argv) == 2:
        if os.environ.get('SLACK_BOT_TOKEN') == None:
            print("Slack token not found in environment variables, make sure the variable is called 'SLACK_BOT_TOKEN'\nUsage: python screenbot.py 'slacktoken' 'channel'")
            exit()

        print("Using slack token from environment variables")
        slack_token = os.environ.get('SLACK_BOT_TOKEN')
        channel = sys.argv[1]
    else:
        slack_token = sys.argv[1]
        channel = sys.argv[2]

    print("Bot is ready")

    client = slack.WebClient(token=slack_token)

    with keyboard.Listener(on_press=on_press) as listener: listener.join()