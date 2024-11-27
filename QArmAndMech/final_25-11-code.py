#--------------------------------------------------------------------------------
import sys
import time
sys.path.append('../')
from Common.standalone_actuator_lib import *
from Common.barcode_checker import *
bot = qbot()
scanner = barcode_checker()
#--------------------------------------------------------------------------------
# RUN THIS SCRIPT TO CONTROL THE ACTUATORS.
#--------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------
bot.activate_linear_actuator()
time.sleep(1)

bot.linear_actuator_out(5)


destination = scanner.barcode.check()

if destination == "Platform A":
    time.sleep(23)
    bot.linear_actuator_in(5)
    time.sleep(5)
    bot.linear_actuator_out(5)

    




## 28
#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------

