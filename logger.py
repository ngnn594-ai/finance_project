import logging
from pathlib import Path

BASE_DIR = Path("data")
FILE_LOGGING = BASE_DIR / "app.log"
BASE_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=FILE_LOGGING,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)



from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"START: {func.__name__}")

        try:
            result = func(*args, **kwargs)
            logger.info(f"END: {func.__name__}")
            return result

        except Exception as e:
            logger.error(f"ERROR in {func.__name__}: {e}")
            raise

    return wrapper