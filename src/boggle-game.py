#!/usr/bin/python3

print("Hello World")

import random
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N=5
x=[
   ['s']*N for i in range(N)
   ]

def scramble_board(g):
    for j in range(N):
        for i in range(N):
            g[j][i] = random.choice(letters)
def stringifyg(g):
    rv=''
    for row in g:
        for cell in row:
            rv+=str(cell)
        rv+='\n'
    rv+='\n'
    return rv

scramble_board(x)
print(stringifyg(g))
print(x)