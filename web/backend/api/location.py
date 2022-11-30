from math import radians, cos, sin, asin, sqrt
import pandas as pd
from api.config import basepath
import os

data = pd.read_json(os.path.join(basepath,'data', 'cameras_data_ip.json'))

def dist(lat1, long1, lat2, long2):
    """
Replicating the same formula as mentioned in Wiki
    """
    # convert decimal degrees to radians 
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    # haversine formula 
    dlon = long2 - long1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

def find_nearest(lat, long):
    data["distances"] = data.apply(
        lambda row: dist(lat, long, row['lat'], row['long']), 
        axis=1)
    data.sort_values(by=['distances'], inplace=True)
    return data.head(7).to_json(orient='records')

