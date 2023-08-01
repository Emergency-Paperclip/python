from pynput import keyboard
import redis

client = redis.Redis(host = "127.0.0.1", port = 6379, decode_responses = True)

key_heald = '0'

def on_press(key):
    global key_heald
    k = '0'
    try:
        k = key.char
    except:
        pass
    if key_heald != '0':
        return
    elif k in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        print(k)
        key_heald = k
        client.publish("square", k)

def on_release(key):
    global key_heald
    key_heald = '0'
    client.publish("square", "0")

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()  # start to listen on a separate thread
listener.join()