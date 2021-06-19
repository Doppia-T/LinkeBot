
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


# does login with credential taken from external file (more actions in the future)
class LinkeBot_BOT:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://linkedin.com/')
        time.sleep(2)

        username = bot.find_element_by_id('session_key')
        password = bot.find_element_by_id('session_password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    # search for a specific "target", like a company or a person, within LinkedIn

    def search_LinkePage(self, target):
        bot = self.bot
        
        import LinkeBot_import_target
        target = LinkeBot_import_target.get_LinkeTarget()
        
        search = bot.find_element_by_xpath("//input[@class='search-global-typeahead__input always-show-placeholder']").click()
        search.send_keys(target)
        search.submit()
        time.sleep(2) 
        
