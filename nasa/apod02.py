#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

#GRAB CREDENTIALS

def returncreds():
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()

    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def main():
    nasacreds = returncreds()

    ##make a call to api
    apodresp = requests.get(NASAAPI + nasacreds)

    apod = apodresp.json()
    print(apod)
    print()
    print(apod["title"] + "\n")
    print(apod["date"] + "\n")
    print(apod["explanation"] + "\n")
    print(apod["url"] + "\n")
    
if __name__ == "__main__":
        main()