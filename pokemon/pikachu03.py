#!/usr/bin/python3

import argparse

import requests

import pandas

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    matchedwords = []

    for item in items.get("results"):
        if args.searchword in item.get("name"):
            matchedwords.append(item.get("name"))

    finishedlist = matchedwords.copy()

    matchedwords = {}
    matchedwords["matched"] = finishedlist

        ## list all words containing matched word
    print(f"There are {len(finishedlist)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print(matchedwords)

    ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(matchedwords)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    itemsdf.to_excel("pokemonitems.xlsx", index=False)
    itemsdf.to_csv("poke.txt", index=False)
    itemsdf.to_json("poke.json")
    
    print("Gotta catch 'em all!")


if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Pass in a word to search the Pokemon item API")
        parser.add_argument('--searchword', metavar='SEARCHW',type=str, default='ball', help="Pass in any word. Default is 'ball'")
        args = parser.parse_args()
        main()