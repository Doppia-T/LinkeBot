import LinkeBot_import_credentials
from LinkeBot_login import LinkeBot_login

#starts process of getting login credentials
LinkeUsername = LinkeBot_import_credentials.get_LinkeID()
LinkePassword = LinkeBot_import_credentials.get_LinkePSS()

#starts process of logging in with the credentials previously obtained
LinkeBot = LinkeBot_login(LinkeUsername,LinkePassword)
LinkeBot.login()

# TEST
# print(LinkeUsername,LinkePassword)