
from LinkeBot_core import LinkeBot_BOT

# ANCILLARY 
# starts process of getting login credentials
import LinkeBot_import_credentials

LinkeUsername = LinkeBot_import_credentials.get_LinkeID()
LinkePassword = LinkeBot_import_credentials.get_LinkePSS()

# PRIMARY
# starts process of logging in with the credentials previously obtained
LinkeBot_login = LinkeBot_BOT(LinkeUsername, LinkePassword)
LinkeBot_login.login()

# ANCILLARY
# starts process of getting a page or a profile (target) to search on LinkedIn
import LinkeBot_import_target

LinkeGetTarget = LinkeBot_import_target.get_LinkeTarget()

# PRIMARY
# start process of searching a page or a profile with the search tool
# of LinkedIn
LinkeBot_search = LinkeBot_BOT(LinkeUsername, LinkePassword)
LinkeBot_search.search_LinkePage(LinkeGetTarget)
