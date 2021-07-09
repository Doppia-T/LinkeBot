from linkebot.core import LinkeBot
from linkebot.handlers import get_linkedin_creds, get_targets
from linkebot.settings import logger


def pipe():
    logger.info("Getting user's credentials.")

    username, password = get_linkedin_creds()

    if not username and password:
        logger.error(
            "Username and password is requried! \
            Check your credentials.yaml file and follow the instructions."
        )

    linebot = LinkeBot(username=username, password=password)

    logger.info("Logging in to linkeding.")
    linebot.login()
    logger.info("Login succesfull.")

    logger.info("Getting the targets.")

    targets = get_targets()

    linebot.search(targets)


if __name__ == "__main__":
    pipe()
