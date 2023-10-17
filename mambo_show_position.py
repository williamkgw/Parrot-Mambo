import db.mongo_interface_mambo as mambo_db
import matplotlib.pyplot as plt
import datetime as dt
import sys

def dim_arr_from_data(axis, data_arr):
    if axis.lower() not in 'xyzt':
        raise(f'Invalid dim({axis}): not(x,y,z,t)')
    
    if axis.lower() == 't':
        return [data['created'] for data in data_arr]
            
    return [data['sensors_dict'][f'DronePosition_pos{axis}'] for data in data_arr]

def get_arr_dim_from_data(data_arr):
    posx = dim_arr_from_data('x', data_arr)
    posy = dim_arr_from_data('y', data_arr)
    posz = dim_arr_from_data('z', data_arr)
    t = dim_arr_from_data('t', data_arr)
    
    return posx, posy, posz, t

def plot_three_graphs(data_arr):

    posx, posy, posz, t = get_arr_dim_from_data(data_arr)
    fig, axs = plt.subplots(3, sharex = True)

    axs[0].set_title('Eixo X')
    axs[0].plot(t, posx, 'ro')
    axs[1].set_title('Eixo Y')
    axs[1].plot(t, posy, 'ro')
    axs[2].set_title('Eixo Z')
    axs[2].plot(t, posz, 'ro')
    plt.show()

def plot_heat_map(data_arr):

    posx, posy, posz, t = get_arr_dim_from_data(data_arr)
    t = [ti.timestamp() for ti in t]
    ax = plt.figure().add_subplot(projection = '3d')

    ax.scatter(posx, posy, posz, s = 200, c = t, cmap = 'hot')
    plt.show()

def main():

    beg_date = dt.datetime(2023, 5, 22)
    end_date = dt.datetime(2023, 5, 24)

    query = {'flying_state': 'landed', 'created': {'$gte': beg_date, '$lte': end_date}}
    projection = {'sensors_dict.DronePosition_posx':True,
                    'sensors_dict.DronePosition_posy':True,
                    'sensors_dict.DronePosition_posz':True,
                    'created': True
                    }

    data_arr = mambo_db.mambo_find_many_in_sensors_collection(query, projection)
    data_arr = [data for data in data_arr]

    if len(sys.argv) != 2:
        raise Exception('CLI argument error')
    
    arg = sys.argv[1]

    if arg == 'heat_map':
        plot_heat_map(data_arr)
    
    if arg == 'three_graphs':
        plot_three_graphs(data_arr)


if __name__ == '__main__':
    main()