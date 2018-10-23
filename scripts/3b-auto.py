#!/usr/bin/python3
# Description: game where you guess a number between 0 and 100 (play's itself)
# Author: Paul hivert
# Date: 15/10/2018

import random

secret = random.randint(0, 100)
count =0
throw = random.randint(0, 100)
while secret != throw:
    throw = random.randint(0, 100)
    count += 1
print("try number: ")
print(count)
print("number that was guessed")
print(secret)