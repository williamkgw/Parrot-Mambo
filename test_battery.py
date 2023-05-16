"""
Demo the trick flying for the python interface

Author: Amy McGovern
"""
from pyparrot.Minidrone import Mambo

def read_file_control():
    with open('control_loop') as file:
        return file.read()

def get_status_mambo(mambo):
    sensors = mambo.sensors
    return sensors.battery, sensors.speed_x, sensors.speed_y, sensors.speed_z

def main():

    mamboAddr = "e0:14:ba:60:3d:c6"
    mambo = Mambo(mamboAddr, use_wifi = False)

    print("trying to connect")
    success = mambo.connect(num_retries=3)
    print("connected: %s" % success)

    if not success:
        return

    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)
    mambo.safe_takeoff(5)

    while read_file_control() != 'parar' and mambo.sensors.battery > 10:

        mambo.hover()
        mambo.smart_sleep(0.5)
        print(get_status_mambo(mambo))    

    mambo.safe_land(5)
    mambo.smart_sleep(5)
    mambo.disconnect()

if __name__ == '__main__':
    main()
