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
