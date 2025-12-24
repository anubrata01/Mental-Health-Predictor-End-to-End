import logging
import os
from datetime import datetime

log_path = os.path.join(os.getcwd(),"logs") # contain logs folder path
os.makedirs(log_path, exist_ok=True)
log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(log_path,log_file)

# formating logging
'''
Placeholder	    Meaning
%(asctime)s	    Time when the log was created
%(lineno)d	    Line number where the log was called
%(name)s	    Logger name (usually module name)
%(levelname)s	Log level (INFO, WARNING, ERROR, etc.)
%(message)s	    The actual log message you wrote

'''

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),  # Logs to file
        logging.StreamHandler()              # Logs to console (THIS WAS MISSING!)
    ]
)
'''
level in logging.basicConfig() controls which types of messages get recorded.
Think of it as a filter — only messages equal or higher than the set level are logged.


Logging Levels (from lowest to highest severity)
Level	    Description	When to use
DEBUG	    Detailed info for developers	For diagnosing issues or understanding internal flow
INFO	    Confirmation that things work as expected	When something starts, completes, or succeeds
WARNING	    Something unexpected happened, but program still runs	Low disk space, missing file fallback
ERROR	    Serious problem — some part failed	Exception during function execution
CRITICAL	Program may crash soon	System failure, unrecoverable errors
'''
