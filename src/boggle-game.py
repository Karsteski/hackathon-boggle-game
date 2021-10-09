import gui_functions
import random

print
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = 5


class Boggle:
    def __init__(self, pname1, pname2):
        self.pname1 = pname1
        self.pname2 = pname2

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
        rv += "\n"
        return rv

    def print(self):
        print(self.stringifyg())


boggle = Boggle("ONE", "TWO")
boggle.scramble_board()
boggle.print()
