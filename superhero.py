#!/usr/bin/env python3



classinfo = {
    "all": [
        {
            "name": "Leo",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Andi",
            "skill level": "admirable",
            "spirit animal": "Shark",
            "super power": "Super Strength",
        },
        {
            "name": "Bianca",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Charlie",
            "skill level": "astonishing",
            "spirit animal": "Banana",
            "super power": "Flight",
        },
        {
            "name": "Cynthia",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "Davi",
            "skill level": "brilliant",
            "spirit animal": "Eagle",
            "super power": "Helicopter Propulsion",
        },
        {
            "name": "Eric",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Jacob",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Immobility",
        },
        {
            "name": "Jim",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Immutability",
        },
        {
            "name": "Paul",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Joseph",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Jet Propulsion",
        },
        {
            "name": "Josia",
            "skill level": "fine",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Kendra",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Mobile Invulnerability",
        },
        {
            "name": "Tito",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Muscle Manipulation",
        },
        {
            "name": "Ryan",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Nail Manipulation",
        },
        {
            "name": "Sabin",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Lawrence",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Organic Constructs",
        },
        {
            "name": "Sharry",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Prehensile Hair",
        },
        {
            "name": "Sheraz",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Prehensile Tail",
        },
        {
            "name": "Sunny",
            "skill level": "remarkable",
            "spirit animal": "Alpaca",
            "super power": "Prehensile Tongue",
        }
    ]
}


def main():
    print(f"My name is {classinfo['all'][11]['name']} and my spirit animal is {classinfo['all'][11]['spirit animal']}.")


    # for i in classinfo:
    #     #  print(f"{i[0]['name']}, a {i[0]['skill level']} {i[0]['spirit animal']} of a programmer, possesses a {i[0]['super power']} factor for moonlighting as a superhero!")
    #     for j in range(len(classinfo[i])):
    #         #print(classinfo[i][j]['name'])
    #         print(f"{classinfo[i][j]['name']}, a {classinfo[i][j]['skill level']} {classinfo[i][j]['spirit animal']} of a programmer, possesses a {classinfo[i][j]['super power']} factor for moonlighting as a superhero!")

    
    # for i in range(len(classinfo["all"])):
    #     print(f"{classinfo['all'][i]['name']}, a {classinfo['all'][i]['skill level']} {classinfo['all'][i]['spirit animal']} of a programmer, possesses a {classinfo['all'][i]['super power']} factor for moonlighting as a superhero!\n")    
    #    # print(classinfo["all"][i])

    for i in classinfo["all"]:
         print(f"{i['name']}, a {i['skill level']} {i['spirit animal']} of a programmer, possesses a {i['super power']} factor for moonlighting as a superhero!\n")    

main()