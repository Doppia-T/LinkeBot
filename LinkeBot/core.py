from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .settings import LINKEDIN_BASE
import time
from selenium.webdriver.firefox.webdriver import WebDriver


class LinkeBot:
    # does login with credential taken from external file (more actions in the future)
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.bot: WebDriver = webdriver.Firefox()

    def login(self) -> None:
        bot = self.bot
        bot.get(LINKEDIN_BASE)
        time.sleep(2)

        username = bot.find_element_by_id("session_key")
        password = bot.find_element_by_id("session_password")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def search(self, targets):
        # search for a specific "target", like a company or a person, within LinkedIn
        bot = self.bot
        for target in targets:
            search = bot.find_element_by_xpath(
                "//input[@class='search-global-typeahead__input always-show-placeholder']"
            ).click()
            search.send_keys(target)
            search.submit()
            time.sleep(2)
