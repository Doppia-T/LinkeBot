import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .settings import BASEDIR, DRIVERNAME, HEADLESS, LINKEDIN_BASE

# from selenium.common.exceptions import TimeoutException

options = Options()
DELAY = 3  # seconds
# options.headless = HEADLESS
if HEADLESS:
    options.add_argument("--headless")


class LinkeBot:
    # does login with credential taken from external file (more actions in the future)
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.bot: WebDriver

    def __enter__(self):
        self.bot: WebDriver = webdriver.Firefox(
            options=options,
            executable_path=BASEDIR / "drivers" / DRIVERNAME,
        )

        return self

    def __exit__(self, type, value, traceback):
        self.bot.quit()

    def login(self) -> bool:
        bot = self.bot
        bot.get(LINKEDIN_BASE)
        login_page: WebDriver = WebDriverWait(bot, DELAY).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sign-in-form-container"))
        )

        username = login_page.find_element_by_id("session_key")
        password = login_page.find_element_by_id("session_password")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        is_error = login_page.find_element_by_class_name("alert")
        return not is_error

    def search(self, target):
        # search for a specific "target", like a company or a person, within LinkedIn
        bot = self.bot

        search = bot.find_element_by_xpath(
            "//input[@class='search-global-typeahead__input always-show-placeholder']"
        ).click()
        search.send_keys(target)
        search.submit()
        time.sleep(2)
