#!/usr/bin/env python3
# Description: inputs a list of names and outputs them
# Author: Paul hivert
# Date: 15/10/2018


import sys
print("enter name or press q to quit")
# infinite loop
loop = 0

liste = []
while loop == 0:
    print("name?")
    value = input()
    try:
        value + 1
    except:
        sys.exit()
    if value == "q":
        liste = sorted(liste)
        for prenom in liste:
            print(prenom)
        break
    else:
        liste.append(value)
