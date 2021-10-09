#!/usr/bin/python3

print("Hello World")

import random
from copy import deepcopy
LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N=5
class Boggle:
    def __init__(self,pv):
        self.pv = pv
        
        self.g=[
               ['-']*N for i in range(N)
               ]

        
    def scramble_board(self):
        for j in range(N):
            for i in range(N):
                self.g[j][i] = random.choice(LETTERS)
    def stringifyg(self):
        rv=''
        for row in self.g:
            for cell in row:
                rv+=str(cell)
            rv+='\n'
        rv+='\n\n'
        return rv
    def print(self):
        print(self.stringifyg())
    def valid_recursive(self,g,y,x,s):
        if s=='' or g[y][x]==None:
            return False
        elif g[y][x]==s:
            return True
        elif g[y][x][0]==s[0]:
            m=len(g)
            n=len(g[0])
            #print("line10")
            g2=deepcopy(g)
            g2[y][x]=None
            for j in range(y-1,y+2):
                for i in range(x-1,x+2):
                    if j<0: continue
                    if j>=m: continue
                    if i<0: continue
                    if i>=n: continue
                    if (j,i)==(y,x): continue
                    if self.valid_recursive(g2,j,i,s[1:]):
                        #print(y,x,s[1:])
                        return True
        return False
    def find_word(self,s):
        for y in range(N):
            for x in range(N):
                if self.g[y][x]==s[0] and self.valid_recursive(deepcopy(self.g),y,x,s): return True
        return False

    def process_player_word_lists(self):
        ui=input("input player word list\n")
        words=ui.split(" ")
        print(words)
        for word in words:
            if self.find_word(word):
                print(word," found in board")
            else:
                print(word," not found")
    def play_round(self):
        self.scramble_board()
        self.print()
        self.process_player_word_lists()
    def play_game(self,rounds):
        for i in range(rounds):
            self.play_round()
        self.determine_winner()
            

boggle=Boggle(["ONE"])
boggle.play_round()
#boggle.print()