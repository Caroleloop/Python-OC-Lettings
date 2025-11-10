import logging
import os
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk import capture_message

# --------------------------------------------------------
# 1. Retrieve SENTRY_DSN from environment variables
# (Never hardcode the DSN in source code)
# --------------------------------------------------------
SENTRY_DSN = os.getenv("SENTRY_DSN")

# --------------------------------------------------------
# 2. Initialize Sentry integration
# --------------------------------------------------------
sentry_logging = LoggingIntegration(
    level=logging.INFO,  # Capture logs >= INFO
    event_level=logging.INFO,  # Convert INFO+ en événements Sentry
)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[sentry_logging],
    traces_sample_rate=1.0,  # Adjust sampling if needed
    environment=os.getenv("APP_ENV", "production"),
)

# --------------------------------------------------------
# 3. Configure local logging
# --------------------------------------------------------
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "application.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler(LOG_FILE),  # Log to file
    ],
)

logger = logging.getLogger("sentry_logger")


# --------------------------------------------------------
# 4. Utility function for logging to local + Sentry
# --------------------------------------------------------
def sentry_log(error_type: str = "", error_message: str = ""):
    """
    Log messages or exceptions locally and/or to Sentry.

    Args:
        error_type (str): Type of log. Possible values:
            - "exception": Log an exception with traceback (captured by Sentry)
            - "message": Send a simple message to Sentry at INFO level
            - "debug": Local debug log
            - "info": Local info log
            - "warning": Local warning log
            - Any other value defaults to error
        error_message (str): The message or exception text to log.

    Behavior:
        - Depending on error_type, logs are sent to local handlers
          and/or Sentry.
    """
    if error_type == "exception":
        logger.exception(error_message)  # Exception + traceback → Sentry auto
    elif error_type == "message":
        capture_message(error_message, level="info")  # Message Sentry direct
    elif error_type == "debug":
        logger.debug(error_message)
    elif error_type == "info":
        logger.info(error_message)
    elif error_type == "warning":
        logger.warning(error_message)
    else:
        logger.error(error_message)
