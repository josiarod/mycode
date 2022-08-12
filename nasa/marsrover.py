#!/usr/bin/python3
import requests

MARSROVERURL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&"


def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    
    #CODE CUSTOMIZATION 01
    earthtdate = input("Enter a earth date in YYYY-MM-DD format: ")

    

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    mars_roler_request = requests.get(MARSROVERURL + earthtdate + "&" +  nasacreds)

    # strip off json attachment from our response
    mars_roler_data = mars_roler_request.json()

    ## display NASAs NEOW data
    print(mars_roler_data)

if __name__ == "__main__":
    main()