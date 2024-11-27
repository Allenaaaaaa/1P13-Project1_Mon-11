ip_address =  "localhost"
project_identifier = 'P3A'
#--------------------------------------------------------------------------------
import sys
from time import sleep
sys.path.append('../')
print(sys.path)
from Common.hardware_project_library import *
from Common.barcode_checker import *

hardware = True
arm = qarm(project_identifier,ip_address,hardware)
table = servo_table(ip_address,None,hardware)
scanner = barcode_checker()

#--------------------------------------------------------------------------------
# STUDENT CODE BEGIN

#-----------------------------------------------------------------------------
    
def reject():
    """
    Drop a luggage off in rejection bin
    """
    pick_up_luggage()
    arm.rotate_base(90)
    # Rotate the base towards the bin (tweak this)
    arm.rotate_base(0)
    arm.rotate_shoulder(0)
    arm.rotate_elbow(0)
    

def platform():
    """
    Drop a luggage on the platform (top of the mechanism)
    """
    pick_up_luggage()
    # Rotate the base towards the platform (tweak this)
    arm.rotate_base(0)
    arm.rotate_shoulder(0)
    arm.rotate_elbow(0)
    

def pick_up_luggage():
    """
    Pick up a luggage from the servo table, then return the arm to the home position without
    droppping the luggage.
    """
    # FACING THE ARM HEAD ON
    arm.home()
    arm.rotate_base(-90) # Rotate to the platform
    arm.rotate_shoulder(0) # positive is down
    arm.rotate_elbow(50) # positive is up
    arm.rotate_wrist(5)
    

def drop_platform():
    arm.rotate_base(90)
    arm.move_arm(0.516, 0, 0.212)

def process_luggage(location):
    # Scan the luggage (on the opposite side of the q-arm)
    location = scanner.barcode_check()
    print(location)

    # Rotate table to position luggage under qarm
    table.rotate_table_angle(180)

    pick_up_luggage()

    if location == 'rejection bin':
        reject()
    else:
        platform()

"""
TEST CODE
"""
pick_up_luggage()

'''
for i in range(1):
    location = scanner.barcode_check()

    print(location)

    arm.home()
    table.rotate_table_angle(180)
    sleep(1)
    if location == 'rejection bin':
        reject()
    else:
        platform()

    sleep(1)
    table.rotate_table_angle(90)
'''
#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------
