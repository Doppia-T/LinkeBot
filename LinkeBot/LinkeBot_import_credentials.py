import os
import sys


#gets username from an external file called "LinCred"
def get_LinkeID():
    with open(os.path.join(sys.path[0], "LinCred.txt"), "r") as find_credential:
        for line in find_credential:
            if line.startswith('id'):
                id_line = line
                spl_word = 'id = '
                spl_id_line = id_line.split(spl_word,1)[1]
                LinkeUsername = spl_id_line
                return LinkeUsername

#gets password from an external file called "LinCred"
def get_LinkePSS():
    with open(os.path.join(sys.path[0], "LinCred.txt"), "r") as find_credential:
        for line in find_credential:
            if line.startswith('password'):
                pss_line = line
                spl_word = 'password = '
                spl_pss_line = pss_line.split(spl_word,1)[1]
                LinkePassword = spl_pss_line
                return LinkePassword