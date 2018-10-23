#!/usr/bin/python3
# Description: game where you guess a number between 0 and 100
# Author: Paul hivert
# Date: 15/10/2018

import sys
import random

secret = random.randint(0, 100)
print("guess a number or q to quit")
guess = input()
try:
    guess = int(guess)
except:
    sys.exit()
while secret != guess:
        if secret < guess:
            print("too big try again")
            guess = int(input())
        elif secret > guess:
            print("too small try again")
            guess = int(input())
        elif guess == "q":
            print("quit")
            print("game ended")
            break
print("la réponse était")
print(secret)