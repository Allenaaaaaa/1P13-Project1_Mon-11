ip_address =  "localhost"
project_identifier = 'P3A'
#--------------------------------------------------------------------------------
import sys
import time
sys.path.append('../')
from Common.hardware_project_library import *
from Common.barcode_checker import *
# from Common.standalone_actuator_lib import *

hardware = True
arm = qarm(project_identifier,ip_address,hardware)
table = servo_table(ip_address,None,hardware)
bot = qbot()
scanner = barcode_checker()

#--------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------


def reject():
    """
    Collect luggage from servo table, then
    drop a luggage off in rejection bin
    """
    pick_up_luggage()
    print("hi")
    arm.rotate_base(90)
    arm.rotate_base(90)
    print("hi")
    arm.control_gripper(-45)
    print("hi")
    

def platform():
    """
    Collect luggage from servo table, then
    drop a luggage on the platform(top of the mechanism)
    """
    pick_up_luggage()
    # Rotate the base towards the platform (tweak this)
    arm.rotate_base(70)
    arm.control_gripper(-45)
    

def pick_up_luggage():
    """
    Pick up a luggage from the servo table, then return the arm to the home position without
    droppping the luggage.
    """
    # FACING THE ARM HEAD ON
    arm.home()
    # Rotate to the platform
    arm.rotate_base(-90)
    # Move the arm down towards the luggage on servo table
    arm.rotate_shoulder(13) # positive is down
    arm.rotate_elbow(22) # positive is up
    # Grab luggage
    arm.control_gripper(45)
    # Move arm up
    arm.rotate_elbow(-32) # positive is up
    

def process_luggage():
    """
    Scan and move a luggage to the correct location
    """
    # Scan the luggage (on the opposite side of the q-arm)
    location = scanner.barcode_check()
    print(location)

    # Rotate table to position luggage under qarm
    table.rotate_table_angle(180)

    if location == 'rejection bin':
        reject()
    else:
        platform()

"""
TEST CODE
"""
#bot.activate_stepper_motor()

for _ in range(4):
    process_luggage()

#bot.rotate_stepper_cw(1.2)
#time.sleep(1)
#bot.rotate_stepper_ccw(1.2)

arm.terminate_arm()

#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------


    

    

