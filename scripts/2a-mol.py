#!/usr/bin/env python3
# Description: game where you guess a number between 0 and 100
# Author: Paul hivert
# Date: 23/10/2018

import sys
import random
import datetime

secret = random.randint(1, 100)
infinity = 0
big = "too big"
small = "too small"
win = "you win"

f = open("2a-write.txt", "r")

lst = f.readline()
lastLine = lst[len(lst)[-1]]

f.write("bienvenue au jeu du + ou -")


if lastLine == secret:
    f.write(win, "a")
elif lastLine < secret:
    f.write(small, "a")
elif lastLine > secret:
    f.write(big, "a")