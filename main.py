"""
Demo the trick flying for the python interface

Author: Amy McGovern
"""

from pyparrot.Minidrone import Mambo

# you will need to change this to the address of YOUR mambo
mamboAddr = "e0:14:ba:60:3d:c6"

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambo = Mambo(mamboAddr, use_wifi = False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    # get the state information
    print("sleeping")
    print('*******')
    mambo.smart_sleep(2)
    print('*******')
    mambo.ask_for_state_update()
    print('*******')
    mambo.smart_sleep(2)
    print('*******')
    print("taking off!")
    mambo.safe_takeoff(5)

    if (mambo.sensors.flying_state != "emergency"):
        print("flying state is %s" % mambo.sensors.flying_state)
        print("Flying direct: going up")
        mambo.hover()
        # mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)

        # print("flip left")
        # print("flying state is %s" % mambo.sensors.flying_state)
        # success = mambo.flip(direction="left")
        # print("mambo flip result %s" % success)
        mambo.smart_sleep(5)

        # print("flip right")
        # print("flying state is %s" % mambo.sensors.flying_state)
        # # success = mambo.flip(direction="right")
        # print("mambo flip result %s" % success)
        # mambo.smart_sleep(5)

        # print("flip front")
        # print("flying state is %s" % mambo.sensors.flying_state)
        # # success = mambo.flip(direction="front")
        # print("mambo flip result %s" % success)
        # mambo.smart_sleep(5)

        # print("flip back")
        # print("flying state is %s" % mambo.sensors.flying_state)
        # # success = mambo.flip(direction="back")
        # print("mambo flip result %s" % success)
        # mambo.smart_sleep(5)

        # print("landing")
        # print("flying state is %s" % mambo.sensors.flying_state)
        speed_x = mambo.sensors.speed_x 
        speed_y = mambo.sensors.speed_y
        speed_z = mambo.sensors.speed_z
        battery = mambo.sensors.battery
        print(battery, speed_x, speed_y, speed_z)

        mambo.safe_land(5)
        mambo.smart_sleep(5)

        speed_x = mambo.sensors.speed_x
        speed_y = mambo.sensors.speed_y
        speed_z = mambo.sensors.speed_z
        battery = mambo.sensors.battery
        print(battery, speed_x, speed_y, speed_z)

print("disconnect")
mambo.disconnect()