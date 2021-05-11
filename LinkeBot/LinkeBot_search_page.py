import os
import sys


# get page to search from external file called "LinTarget"
def get_LinkePage():
    with open(os.path.join(sys.path[0], "LinTarget.txt"), "r") as find_target:
        for line in find_target:
            LinkeTarget = line
            return LinkeTarget

# start research of page
