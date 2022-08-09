#!/usr/bin/python3

import random
import crayons
import requests
from emoji import emojize
# pip install emoji

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                   'north' : 'Laundry room',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            },

            'Laundry room' : {
                'south' : 'Hall',
                'item'  : 'flamethrower',
            }
         }


room_names = ['Pantry','Garden','Dining Room', 'Hall', 'Laundry room']
#start the player in the Hall
currentRoom = room_names[random.randint(0, len(room_names) - 1)]

showInstructions()


question = requests.get('https://opentdb.com/api.php?amount=1&type=boolean')
question = question.json()


#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print(crayons.red('You can\'t go that way!'))

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print(crayons.yellow('Can\'t get ' + move[1] + '!'))
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print(crayons.blue('You escaped the house with the ultra rare key and magic potion... YOU WIN!'))
    break
  elif 'key' in inventory:
      print("Welcome to the garden I see you have the key, but to dine with the king you will need some magic... ")
      print("Go back in the house.")
  elif 'potion' in inventory:
      print('I see some magic in you.')
      print('Answer this question to reveal the ',end="")
      print(emojize(":key:"))
      print(question['results'][0]['question'])
      answer = input(crayons.red("Enter True or False\n"))

      if answer == question["results"][0]['correct_answer']:
          print(crayons.green("The key is in the hall"))
      else:
          print(crayons.blue("Today is not your day."))   

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    #if flamethrower is in the inventory player can kill the monster
    #monster is removed from items
      if 'flamethrower' in inventory:
          print(emojize(":alien_monster:"))
          print(crayons.yellow('Oh oh there is a monster here\n'))
          print('Using the flamethrower to kill the monster ', end="")
          print(emojize(":fire:"))
          print('Hasta la vista BABY ', end="")
          print(emojize(":smiling_face_with_sunglasses:"))
          del rooms[currentRoom]['item']
      else:
         print(emojize(":alien_monster:"))
         print('A monster has got you... GAME OVER!')
         break