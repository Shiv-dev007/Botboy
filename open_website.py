from chat_history import history
import time
import webbrowser

def open_webites(user):
    user = user

    if "youtube" in user or "yt" in user or "openyt" in user or "openyoutube" in user:
        print("Botboy: Opening youtube sir.....")
        time.sleep(0.5)
        webbrowser.open("https://youtube.com")
        reply =  "Opened youtube for you sir......"
        history(user,reply)
    elif "github" in user or "opengithub" in user:
        print("Botboy: Opening Github sir.....")
        time.sleep(0.5)
        webbrowser.open("https://github.com")
        reply =  "Opened github for you sir......"
        history(user,reply)

    return reply