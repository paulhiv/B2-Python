#!/usr/bin/env python3
# Description: game where you guess a number between 0 and 100
# Author: Paul hivert
# Date: 23/10/2018

import random
import time
import sys

secret = random.randint(1, 100)
inputCheck = False
success = False
big = "too big\n"
small = "too small\n"
win = "you win\n"

while success is not True:
    with open("2a-write.txt", "r") as f:
        lst = f.readlines()
        lastLine = lst[len(lst) - 1]

    with open("2a-write.txt", "w") as f:
        f.write("bienvenue au jeu du + ou -\n")

    while inputCheck is not True:
        try:
            lastLine = int(lastLine)
            inputCheck = True

        except Exception as e:
            sys.stdout.write(str(e))
            sys.stdout.write("écrivez votre numéro à la fin du ficher 2a-mol.py vous avez 5 secondes\n")
            time.sleep(5)

            with open("2a-write.txt", "r") as f:
                lst = f.readlines()
                lastLine = lst[len(lst) - 1]

    if inputCheck is True:
        inputCheck = False

    if lastLine == secret:
        with open("2a-write.txt", "w") as f:
            f.write(win)
        success = True

    elif lastLine < secret:
        with open("2a-write.txt", "w") as f:
            f.write(small)

    elif lastLine > secret:
        with open("2a-write.txt", "w") as f:
            f.write(big)
