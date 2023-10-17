import json
from pathlib import Path

CONFIG_DIR = 'config'
CONFIG_FILE = 'env.json'

def file_config():
    file_path = f'{CONFIG_DIR}/{CONFIG_FILE}'
    return Path(file_path)

def read_json():
    file = file_config()

    with open(file, 'r') as json_file:
        data = json.load(json_file)
    
    return data

def search_in_array_for_dict(arr, key, value):
    
    for element in arr:
        if value == element.get(key):
            return element

    return None

def running_config():
    return read_json()['running']

def clusters():
    return read_json()['dbs']

def mongodb_cluster():
    clusters_dbs = clusters()
    return search_in_array_for_dict(clusters_dbs, "nome", "mongodb")

def database_from_cluster(cluster, database):
    return search_in_array_for_dict(cluster['databases'], "nome", database)

def drones():
    return read_json()['drones']

def search_drone(id_drone):
    return search_in_array_for_dict(drones(), 'id', id_drone)

def main():
    print(search_drone(1))

if __name__ == '__main__':
    main()