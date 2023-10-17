from pymongo import MongoClient
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter



def project_columns():
    return {
        'battery': True,
        'speed_x': True,
        'speed_y': True,
        'speed_z': True,
        'created': True
        }

def query_columns():
    return {
        'flying_state': 'hovering',
    }

client = MongoClient("mongodb://localhost:27017/")
db = client['mambo_drone']

data = db.sensors.find(query_columns(), project_columns())
df = pd.DataFrame(list(data))



amostra_df = df[(df['created'] > '2023-05-23') & (df['created'] < '2023-05-24')]
init_time = amostra_df.iloc[0, -1]
amostra_df['time'] = amostra_df['created'] - init_time
amostra_df['time'] = amostra_df['time'].dt.total_seconds()

amostra_df[['battery', 'time']].to_csv('hovering.csv')

amostra_df.plot(x = 'time', y = 'battery', kind = 'scatter')
plt.show()