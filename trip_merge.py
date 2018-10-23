import pandas as pd

df_trip = pd.read_csv("C:/YenTingPC/Python_project/sf_bike/trip.csv")
df_station = pd.read_csv("C:/YenTingPC/Python_project/sf_bike/station.csv")


df_station_prime = df_station.loc[:,['id','lat','long']]
df_station_start = df_station_prime.rename(columns={'id': 'start_station_id', 'lat': 'start_lat', 'long': 'start_long'})
df_station_end = df_station_prime.rename(columns={'id': 'end_station_id', 'lat': 'end_lat', 'long': 'end_long'})

df_join = pd.merge(df_trip, df_station_start, how='left', on='start_station_id')
df_join = pd.merge(df_join, df_station_end, how='left', on='end_station_id')

df_join.to_csv('trip_join.csv', index=0)

