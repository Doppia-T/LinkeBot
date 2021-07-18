from linkebot.core import LinkeBot
from linkebot.handlers import get_linkedin_creds, get_targets
from linkebot.settings import logger


def pipe() -> None:

    logger.info("Getting user's credentials.")

    username, password = get_linkedin_creds()

    if not username and password:
        logger.error(
            "Username and password is requried! \
            Check your credentials.yaml file and follow the instructions."
        )

    logger.info("Launching linkebot driver.")
    with LinkeBot(username=username, password=password) as linkebot:
        logger.info("Logging in to linkedin.")
        logged_in = linkebot.login()
        if not logged_in:
            logger.info("Error during login.")

            return
        logger.info("Login succesfull.")

        logger.info("Getting the targets.")

        targets = get_targets()

        linkebot.search(targets)

        logger.info("Operation completed!")
        return


if __name__ == "__main__":
    pipe()
