import random
from copy import deepcopy

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = 5
SCORING_RULES = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}
for i in range(12, 37):
    SCORING_RULES[i] = 11

# debugging function. creates a 2d vector by splitting by - then spaces
def parse_ui(ui):
    wordlist2d = ui.split("-")
    rv = []
    for wordlist in wordlist2d:
        rv.append(wordlist.split(" "))
    return rv


# The Boggle object contains the state of the game and provides functions
# to manipulate the game state to play. scramble(), scoring etc
class Boggle:
    def __init__(self, pv):
        self.pnames = pv
        self.scores = [0 for e in pv]
        self.round_scores = [0 for e in pv]
        self.g = [["-"] * N for i in range(N)]

    def scramble_board(self):
        for j in range(N):
            for i in range(N):
                self.g[j][i] = random.choice(LETTERS)

    def stringifyg(self):
        rv = ""
        for row in self.g:
            for cell in row:
                rv += str(cell)
            rv += "\n"
        rv += "\n\n"
        return rv

    def print(self):
        print(self.stringifyg())

    # determins if a player provided word does in fact exist in some possible
    # in the grid. works recursively by checking one character and then
    # recurses all neighbors with a substring
    # elements get changed to None to prevent cell reuse
    def valid_recursive(self, g, y, x, s):
        if s == "" or g[y][x] == None:
            return False
        elif g[y][x] == s:
            return True
        elif g[y][x][0] == s[0]:
            m = len(g)
            n = len(g[0])
            g2 = deepcopy(g)
            g2[y][x] = None
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if j < 0:
                        continue
                    if j >= m:
                        continue
                    if i < 0:
                        continue
                    if i >= n:
                        continue
                    if (j, i) == (y, x):
                        continue
                    if self.valid_recursive(g2, j, i, s[1:]):
                        return True
        return False
    # helper function that sets up the recursive function
    # starts looking at every cell
    def find_word(self, s):
        for y in range(N):
            for x in range(N):
                if self.valid_recursive(deepcopy(self.g), y, x, s):
                    return True
        return False

    # takes in a 2d vector, a list for each player
    def process_player_word_lists(self, player_word_lists):
        self.round_scores = [0 for e in self.pnames]
        print("round_scores=",self.round_scores)
        for i, words in enumerate(player_word_lists):
            for word in words:
                if word == "":
                    continue
                if self.find_word(word):
                    print(word, " found in board")
                    # OMG, what if more than one "Q herp a derp!
                    if "Q" in word:
                        size=len(word)+1
                    else:
                        size=len(word)
                    self.round_scores[i] += SCORING_RULES[size]
                    print("round_scores=",self.round_scores)
                else:
                    print(word, " not found")
        maxi, max = 0, self.round_scores[0]
        # Ved, maybe you wanna refactor this to make it more pythonic?
        # finds winner and if tie
        for j in range(1, len(self.round_scores)):
            if self.round_scores[j] > max:
                maxi, max = j, self.round_scores[j]
                print("maxi=",maxi,"max=",max)
        if self.round_scores.count(max) > 1:
            winners = []
            for j, score in enumerate(self.round_scores):
                if score == max:
                    winners.append(self.pnames[j])
            print("TIE!\nCONGRATULATIONS TO", " ".join(winners))
        else:
            print(self.pnames[maxi], "Won with", self.round_scores[maxi], "points.")
        for i,score in enumerate(self.round_scores):
            self.scores[i]+=score
    def ui_player_word_lists(self):
        ui = input("input player word lists. - is separator\n")
        pui =  parse_ui(ui)
        print(pui)
        return pui
    
    # Actually I believe these gameplay loop functions should be replaced
    # by gui functions
    def play_round(self):
        self.scramble_board()
        self.print()
        # GUI code here to populate wordlists
        wordlists = self.ui_player_word_lists()
        self.process_player_word_lists(wordlists)
    def determine_winner(self):
        maxi, max = 0, self.scores[0]
        # Ved, maybe you wanna refactor this to make it more pythonic?
        # finds winner and if tie
        for j in range(1, len(self.scores)):
            if self.scores[j] > max:
                maxi, max = j, self.scores[j]
                print("maxi=",maxi,"max=",max)
        if self.scores.count(max) > 1:
            winners = []
            for j, score in enumerate(self.scores):
                if score == max:
                    winners.append(self.pnames[j])
            print("GAME TIE!\nCONGRATULATIONS TO", " ".join(winners))
        else:
            print(self.pnames[maxi], "Won game with", self.scores[maxi], "points total.")
        
    def play_game(self, rounds):
        for i in range(rounds):
            print("ROUND {}!".format(i+1))
            self.play_round()
        self.determine_winner()

if __name__ == "__main__":
    boggle = Boggle(["ONE","TWO"])
#    boggle.pv=["x","y"]
#    boggle.play_round()
#    print(boggle.g,boggle.pv,boggle.scores)
#    boggle.scramble_board()
#    print(boggle.pv[1])
#    boggle.pv[1]="BRAVO"
#    print(boggle.g,boggle.pv,boggle.scores)
    boggle.play_game(2)
    