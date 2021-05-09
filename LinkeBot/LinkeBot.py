from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
import time


#gets username from an external file called "LinCred"
def get_LinkeID():
    with open(os.path.join(sys.path[0], "LinCred.txt"), "r") as find_cred:
        for line in find_cred:
            if line.startswith('id'):
                id_line = line
                spl_word = 'id = '
                spl_id_line = id_line.split(spl_word,1)[1]
                LinkeUsername = spl_id_line
                return LinkeUsername

#gets password from an external file called "LinCred"
def get_LinkePSS():
    with open(os.path.join(sys.path[0], "LinCred.txt"), "r") as find_cred:
        for line in find_cred:
            if line.startswith('password'):
                pss_line = line
                spl_word = 'password = '
                spl_pss_line = pss_line.split(spl_word,1)[1]
                LinkePassword = spl_pss_line
                return LinkePassword


#does login with credential taken from external file (more actions in the future)
class LinkeBot:
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
        #time.sleep(3)

    def like_post(self,profile):
        bot = self.bot
        bot.get('https://www.linkedin.com/in/'+profile+'/') #insert the "def" for where to get the profile
        time.sleep(2)


#starts process of getting login credentials
get_LinkeID()
LinkeUsername = get_LinkeID()
get_LinkePSS()
LinkePassword = get_LinkePSS()

#starts process of logging in with the credentials previously obtained
TestBot = LinkeBot(LinkeUsername,LinkePassword)
TestBot.login()

#feature under development
#TestBot.like_post('null')
