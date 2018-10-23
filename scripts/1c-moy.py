#!/usr/bin/env python3
# Description: inputs a name paired with a grade and outputs the class average
# Author: Paul hivert
# Date: 15/10/2018
import sys

print("saisissez votre note ensuite votre prenom")

# creates an empty dictionary
dictionary = {}
# infinite loop
loop = 0
# variable to scope out the values in the dictionary
sum = 0
# counter to get the top 5
a = 0

while loop == 0:
    print("saisissez un prenom")
    nom = input()
    if nom == "q":
        print("liste des notes")
# loop to access each value in the dictionary
        for liste in sorted(dictionary):
            full = dictionary[liste]
            print(full)
# scope out the sum of all grades
            sum += int(full)
        print("moyenne est égale a ")
        moy = sum / len(dictionary)
        try:
            moy == int(moy)
        except:
            sys.exit("please enter a grade")
        print(moy)
        sum = 0
        print("moyenne top 5 est égale a ")
        for top in dictionary:
            while a != 4:
                a += 1
                sum =+ int(dictionary[top])
        moy = sum / 5
        print(moy)
        break
    else:
        print("saisissez votre note")
        note = input()
        dictionary[nom] = note