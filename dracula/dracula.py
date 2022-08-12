#!/usr/bin/python3

with open("dracula.txt", "r") as dracula:
    counter = 0
    for line in dracula:
        if "vampire" in line.lower():
            print(line)
            counter += 1
    print(counter)