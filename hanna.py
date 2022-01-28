import pygame as pg
import random
from random import randint
import numpy as np

nb_lines = 10
nb_columns = 10

screen = []
for i in range(nb_lines):
    screen += [[' ' for k in range(nb_columns)]]

x,y = random.randint(1, nb_columns-2), random.randint(1, nb_lines-2)
vertical = random.randint(2, nb_lines-y-1)

horizontal = random.randint(2, nb_columns-x-1)

print((x, y))
print((vertical, horizontal))

for k in range(horizontal+1) :
    screen[x][y+k] = '-'
    screen[x+vertical][y+k] = '-'
for j in range(1, vertical) :
    screen[x+j][y] = '|'
    screen [x+j][y+horizontal] = '|'
for k in range(1, vertical):
    for j in range(1, horizontal):
        screen[x+k][y+j] = '.'

for line in screen :
    print(line)
