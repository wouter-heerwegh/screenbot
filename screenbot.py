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

    save = input("Would you like to store/edit your token and/or channel? (y/N): ")
    while True:
        if str(save).lower() == 'y':
            token = input("Slack bot token (leave empty if you don't want to change it): ")
            if token != "":
                setenv_var("SLACK_BOT_TOKEN", token)
            chan = input("Slack channel (leave empty if you don't want to change it): ")
            if chan != "":
                setenv_var("SLACK_CHANNEL", chan)

        if os.environ.get('SLACK_BOT_TOKEN') == None or os.environ.get('SLACK_CHANNEL') == None:
            print("Slack token not found in environment variables, make sure the variable is called 'SLACK_BOT_TOKEN' and 'SLACK_CHANNEL'\n")
        else:
            break

    slack_token = os.environ.get('SLACK_BOT_TOKEN')
    channel = os.environ.get('SLACK_CHANNEL')

    print("Bot is ready")
    print("Press the 'print screen' button to send a screenshot, press 'escape' to quit")

    client = slack.WebClient(token=slack_token)

    with keyboard.Listener(on_press=on_press) as listener: listener.join()
