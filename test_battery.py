"""
Demo the trick flying for the python interface

Author: Amy McGovern
"""

from pyparrot.Minidrone import Mambo
import db.mongo_interface_mambo as mongo_db
import config.data_interface_json as config
    
def callback_database_sensors(args_sensors):
    if len(args_sensors) != 1:
        raise Exception('Argument Error: args_sensors')

    print('trouxa')
    mambo_sensors = args_sensors[0]
    data_sensors = mongo_db.mambo_get_data_to_insert_in_collection_sensors(mambo_sensors)
    # print(data_sensors)
    mongo_db.mambo_insert_in_sensors_collection(data_sensors)

def main():
    id_drone = config.running_config()['id_drone']
    drone_data = config.search_drone(id_drone)

    mamboAddr = drone_data['addr']
    mambo = Mambo(mamboAddr, use_wifi = False)
    sensors_collection = mongo_db.mambo_sensors_collection()

    print("trying to connect")
    success = mambo.connect(num_retries=3)
    print("connected: %s" % success)

    if not success:
        return

    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)
    mambo.safe_takeoff(5)

    try:
        mambo.sensors.set_user_callback_function(callback_database_sensors, (mambo.sensors,))
        mambo.hover()
        while True:
            mambo.takeoff()
            mambo.hover()
            print('Enviando dados para o mongoDB')

    except BaseException as e:
        print(e)

    mambo.safe_land()
    mambo.smart_sleep(5)
    mambo.disconnect()

if __name__ == '__main__':
    main()
