#!/usr/bin/python3

from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

#allows users to turn their last roll into a 6
class Cheat_Swapper(Player): #inherits player
    def cheat(self):
        self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1


class Cheat_Dice_Mult(Player):
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 4:
                self.dice[i] *= 2
            i += 1