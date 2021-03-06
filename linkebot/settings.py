import sys
from pathlib import Path

from loguru import logger

PROJECTNAME = "linkebot"

BASEDIR = Path(__file__).resolve().parent.parent
CONFIGDIR = BASEDIR / "config"
OUTPUTDIR = BASEDIR / "output"

# Loguru config
logger.remove()
logger.add(
    BASEDIR / f"{PROJECTNAME}.log",
    enqueue=True,
    backtrace=True,
)
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time}</green> <level>{message}</level>",
    level="INFO",
)


# URLS
LINKEDIN_BASE = "https://linkedin.com/"
HEADLESS = False
DRIVERNAME = "geckodriver.exe"
