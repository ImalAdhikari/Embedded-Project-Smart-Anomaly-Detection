import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log" # Log file name includes timestamp to ensure uniqueness and easy identification of when logs were generated.
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE) # Constructs the full path to the log file by joining the current working directory, a 'logs' subdirectory, and the log file name.
os.makedirs(logs_path, exist_ok=True) # Ensures that the 'logs' directory exists; if it doesn't, it will be created. The 'exist_ok=True' parameter prevents an error if the directory already exists.


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # Final path to the log file where logs will be written.

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)# Sets the logging level to INFO, meaning that all messages at this level and above (WARNING, ERROR, CRITICAL) will be logged.\


if __name__ == "__main__":
    logging.info("Logging has been configured successfully.")
    # This block is for testing the logging setup. When this script is run directly, it will log an informational message confirming that logging is configured and showing the path to the log file.