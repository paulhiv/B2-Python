#!/usr/bin/python3
# Description: gives the sum of 2 numbers
# Author: Paul hivert
# Date: 15/10/2018

import sys
print("choisi un nombre")
value1 = input()
try:
    value1 = int(value1)
except:
    sys.exit("please enter a number")
print("choisi un autre nombre")
value2 = input()
try:
    value2 = int(value2)
except:
    sys.exit("please enter a number")

print("leurs somme est égale a ")
print(value1 + value2)