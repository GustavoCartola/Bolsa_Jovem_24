import ephem
from datetime import datetime, timedelta

def next_full_moon(location):
    observer = ephem.Observer()
    observer.lat, observer.lon = location
    next_full_moon_date = ephem.next_full_moon(datetime.now())
    observer.date = next_full_moon_date
    return observer.date.datetime() + timedelta(hours=-3)  #fuso horário de Fortaleza (UTC-3)

#Coordenadas de Fortaleza, CE
fortaleza_location = ('-3.71722', '-38.5434')

print("A próxima lua cheia em Fortaleza será em:", next_full_moon(fortaleza_location))