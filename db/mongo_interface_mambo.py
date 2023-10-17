import db.mongo as mongo
import datetime as dt
import config.data_interface_json as config

def get_now_timestamp():
    return dt.datetime.now()

def mambo_start_client_database_connection():
    cluster = config.running_config()['cluster']
    uri = config.search_in_array_for_dict(config.clusters(), 'nome', cluster)['uri']
    
    return mongo.start_client_database_connection(uri)

def mambo_database():
    database = config.running_config()['database']
    return mongo.database(mambo_start_client_database_connection(), database)

def mambo_sensors_collection():
    return mongo.collection(mambo_database(), 'sensors')

def mambo_insert_in_sensors_collection(data):
    return mongo.insert_in_collection(mambo_sensors_collection(), data)

def mambo_insert_many_in_sensors_collection(data):
    return mongo.insert_many_in_collection(mambo_sensors_collection(), data)

def mambo_find_in_sensors_collection(query, projection):
    return mongo.find_in_collection(mambo_sensors_collection(), query, projection)

def mambo_find_many_in_sensors_collection(query, projection):
    return mongo.find_many_in_collection(mambo_sensors_collection(), query, projection)

def mambo_get_data_to_insert_in_collection_sensors(mambo_sensors):
    return {
        'battery': mambo_sensors.battery, 
        # drone on the ground
        'flying_state': mambo_sensors.flying_state, 
        # dictionary for extra sensors
        'sensors_dict': mambo_sensors.sensors_dict, 

        'gun_id': mambo_sensors.gun_id, 
        'gun_state': mambo_sensors.gun_state, 

        'claw_id': mambo_sensors.claw_id, 
        'claw_state': mambo_sensors.claw_state, 

        'flying_mode': mambo_sensors.flying_mode, 
        'plane_gear_box': mambo_sensors.plane_gear_box, 
        # new SDK sends speed, altitude, and quaternions
        'speed_x': mambo_sensors.speed_x, 
        'speed_y': mambo_sensors.speed_y, 
        'speed_z': mambo_sensors.speed_z, 
        'speed_ts': mambo_sensors.speed_ts, 
        # these are only available on wifi
        'altitude': mambo_sensors.altitude, 
        'altitude_ts': mambo_sensors.altitude_ts, 
        'quaternion_w': mambo_sensors.quaternion_w, 
        'quaternion_x': mambo_sensors.quaternion_x, 
        'quaternion_y': mambo_sensors.quaternion_y, 
        'quaternion_z': mambo_sensors.quaternion_z, 
        'quaternion_ts': mambo_sensors.quaternion_ts,

        # time of the day used
        'created': get_now_timestamp()
        }
