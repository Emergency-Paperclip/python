from pynput import keyboard
import redis

notes = {"C4": 261.63, "D4": 293.66, "E4": 329.63, "F4": 349.23, "G4": 392, "A4": 440, "B4": 493.88}

client = redis.Redis(host = "127.0.0.1", port = 6379, decode_responses = True)

key_heald = '-1'

def on_press(key):
    global key_heald
    k = '0'
    try:
        k = key.char
    except:
        pass
    if key_heald != '-1':
        return
    elif k in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        key_heald = k
        note = str(k.upper() + "4")
        client.publish("square", notes[note])

def on_release(key):
    global key_heald
    key_heald = '-1'
    client.publish("square", "-1")

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()  # start to listen on a separate thread
listener.join()