import os
from collections import Counter
import time
import logging
import signal

LOG_FILE_PATH = "log-file.txt"  
KEYWORDS = ["ERROR", "WARNING"] 


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def signal_handler(sig, frame):
    print("\nMonitoring stopped.")
    exit(0)

# monitor log file
def monitor_log_file():
    try:
        with open(LOG_FILE_PATH, "r") as file:
            file.seek(0, os.SEEK_END)
            while True:
                line = file.readline()
                if line:
                    print(line.strip()) 
                    analyze_log_entry(line)  
                time.sleep(0.1) 
    except FileNotFoundError:
        logger.error("Log file not found.")
        exit(1)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        exit(1)

#  analyze log entry
def analyze_log_entry(entry):
    for keyword in KEYWORDS:
        if keyword in entry:
            logger.info(f"Found keyword '{keyword}' in log entry: {entry}")

def main():
    signal.signal(signal.SIGINT, signal_handler)
    logger.info("Log monitoring started...")
    monitor_log_file()

if __name__ == "__main__":
    main()
