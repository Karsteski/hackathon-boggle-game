#!/usr/bin/python3

print("Hello World")

import random
from copy import deepcopy
LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N=5
SCORING_RULES={0:0,1:0,2:0,3:1,4:1,5:2,6:3,7:5,8:11}
for i in range(12,37):
    SCORING_RULES[i]=11
    
def parse_ui(ui):
    wordlist2d=ui.split("-")
    rv=[]
    for wordlist in wordlist2d:
        rv.append(wordlist.split(" "))
    return rv
class Boggle:
    def __init__(self,pv):
        self.pv = pv
        self.scores = [ 0 for e in pv]
        
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

    def process_player_word_lists(self,player_word_lists):
        round_scores = [0 for e in self.pv]            
        for i,words in enumerate(player_word_lists):
            for word in words:
                if self.find_word(word):
                    print(word," found in board")
                    
                    round_scores[i]+=SCORING_RULES[len(word)]
                else:
                    print(word," not found")
        maxi,max = 0,round_scores[0]
        for j in range(1,len(round_scores)):
            if round_scores[j]>max:
                maxi,max=j,round_scores[j]
        if round_scores.count(max)>1:
            winners=[]
            for j,score in enumerate(round_scores):
                if score==max:
                    winners.append(pv[j])
            print("TIE!\nCONGRATULATIONS TO"," ".join(winners))
        else:
            print(pv[maxi],"Won with",round_scores[maxi],"points.")
    def ui_player_word_lists(self):
        ui=input("input player word lists. - is separator\n")
        return parse_ui(ui)
    def play_round(self):
        self.scramble_board()
        self.print()
        wordlists = self.ui_player_word_lists()
        self.process_player_word_lists(wordlists)
        
    def play_game(self,rounds):
        for i in range(rounds):
            print("ROUND {}!".format(i))
            self.play_round()
        self.determine_winner()
            

boggle=Boggle(["ONE"])
boggle.play_round()
#boggle.print()