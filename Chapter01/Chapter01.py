from datetime import datetime
from os import getcwd
import sys
import time
import random

whoAmI = getcwd()
print(whoAmI)
print(sys.platform)
print(sys.getdefaultencoding())
print(sys.getprofile())
print(sys.getwindowsversion())
print(sys.platform)
print(sys.version)
print(sys.version_info)


odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
 21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for index in range(5):
    sleepTimeInSeconds = random.randint(0, 60)
    print("Sleep time: ")
    print(sleepTimeInSeconds)
    time.sleep(sleepTimeInSeconds)
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")



