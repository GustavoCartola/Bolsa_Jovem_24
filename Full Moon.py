import ephem
from datetime import datetime, timedelta

def next_full_moon(location):
    observer = ephem.Observer()
    observer.lat, observer.lon = location  # set observer's latitude and longitude
    next_full_moon_date = ephem.next_full_moon(datetime.now())  # calculate the next full moon date
    observer.date = next_full_moon_date
    return observer.date.datetime() + timedelta(hours=-3)  # adjust for Fortaleza's time zone (UTC-3)

# Coordinates for Fortaleza, CE
fortaleza_location = ('-3.71722', '-38.5434')

print("A próxima lua cheia em Fortaleza será em:", next_full_moon(fortaleza_location))  # display the next full moon date for Fortaleza
