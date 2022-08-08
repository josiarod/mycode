#!/usr/bin/python3 

import requests

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    #Call the webserver
    groundctrk = requests.get(MAJORTOM)
    helmetson = groundctrk.json()

    print("\n\nConverted python data")
    print(helmetson)

    print("\n\nPeople in Space: ", helmetson['number'])
    people = helmetson['people']
    
    
    for person in people:
        print(f"{person['name']} on the {person['craft']}")

if __name__ == "__main__":
    main()