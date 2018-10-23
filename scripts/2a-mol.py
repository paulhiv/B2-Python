#!/usr/bin/env python3
# Description: game where you guess a number between 0 and 100
# Author: Paul hivert
# Date: 23/10/2018


import random
import time

secret = random.randint(1, 100)
success = False
big = "too big\n"
small = "too small"
win = "you win"
while success is not True:
    f = open("2a-write.txt", "r")

    lst = f.readlines()
    lastLine = lst[len(lst) - 1]
    f.close()
    f = open("2a-write.txt", "w")
    f.write("\nbienvenue au jeu du + ou -\n")
    f.close()

    try:
        lastLine == int(lastLine)
    except Exception as e:
            print(str(e))
            print("écrivez votre numéro a la fin du ficher 2a-mol.py vous avez 10 secondes\n")
            time.sleep(10)
            f = open("2a-write.txt", "r")
            lst = f.readlines()
            f.close()
            lastLine = lst[len(lst) - 1]

    lastLine = int(lastLine)

    if lastLine == secret:
        with open("2a-write.txt", "w") as f:
            f.write(win)
            f.write("\n")
        success = True

    elif lastLine < secret:
        with open("2a-write.txt", "w") as f:
            f.write(small)
            f.write("\n")

    elif lastLine > secret:
        with open("2a-write.txt", "w") as f:
            f.write(big)
            f.write("\n")
