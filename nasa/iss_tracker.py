#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import time
import reverse_geocoder as rg   
URL= "http://api.open-notify.org/iss-now.json"



def main():
    resp= requests.get(URL).json()
    
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    timestamp = resp["timestamp"]
    
    coords_tuple= (lat, lon)
    city_country = rg.search(coords_tuple)
    city = city_country[0]['cc']
    country = city_country[0]['name']
    human_time = time.strftime('%a, %d %b %Y %H:%M:%S %Z',time.localtime(timestamp))
    print("CURRENT LOCATION OF THE ISS: ")
    print(f"Timestamp: {human_time}")
    print(f"Lon: {lon}")
    print(f"Lat: {lat}")

    print(f"City/Country: {country}, {city} ")





if __name__ == "__main__":
    main()