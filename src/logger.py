import logging 
import os
from datetime import datetime

# Correct timestamp format for month
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define logs directory (without file)
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)  # Create only the directory

# Define full log file path
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Create logger instance
logger = logging.getLogger(__name__)


