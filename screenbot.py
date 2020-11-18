from pynput import keyboard
import slack, os, pyautogui, sys, win32api, win32con

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
        sys.exit()

def setenv_var(varname, value):
    try:
        rkey = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment',0 ,win32con.KEY_WRITE)
        try:
            win32api.RegSetValueEx(rkey, varname, 0, win32con.REG_SZ, value)
            print("Saved ", varname)
            return True
        except Exception:
            pass
    except Exception:
        print("No access to save environment variables, if you want to save them, please run this once in administrator mode")
        print("Running bot without save\n")
    finally:
        try:
            win32api.RegCloseKey(rkey)
        except UnboundLocalError:
            pass
    return False

if __name__ == "__main__":
    slack_token = ''
    channel = ''

    if len(sys.argv) == 1 :
        if os.environ.get('SLACK_BOT_TOKEN') == None or os.environ.get('SLACK_CHANNEL') == None:
            print("Slack token not found in environment variables, make sure the variable is called 'SLACK_BOT_TOKEN' and 'SLACK_CHANNEL'\nUsage: python screenbot.py 'slacktoken' 'channel'")
            sys.exit()

        slack_token = os.environ.get('SLACK_BOT_TOKEN')
        channel = os.environ.get('SLACK_CHANNEL')
    elif len(sys.argv) == 2:
        if os.environ.get('SLACK_BOT_TOKEN') == None:
            print("Slack token not found in environment variables, make sure the variable is called 'SLACK_BOT_TOKEN'\nUsage: python screenbot.py 'slacktoken' 'channel'")
            sys.exit()

        print("Using slack token from environment variables")
        slack_token = os.environ.get('SLACK_BOT_TOKEN')
        channel = sys.argv[1]
    else:
        x = input("Do you want to save these variables? (y/N): ")
        if str(x).lower() == 'y':
            setenv_var("SLACK_BOT_TOKEN", sys.argv[1])
            setenv_var("SLACK_CHANNEL", sys.argv[2])
        slack_token = sys.argv[1]
        channel = sys.argv[2]

    print("Bot is ready")

    client = slack.WebClient(token=slack_token)

    with keyboard.Listener(on_press=on_press) as listener: listener.join()
