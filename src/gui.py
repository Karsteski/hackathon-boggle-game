from gui_functions import *
from boggle_game import *


# Test Grid
test_grid = [["a", "f"], ["b", "g"], ["c", "h"], ["d", "i"], ["e", "j"]]

boggle=Boggle(["ALICE"])
boggle.scramble_board()
print(boggle.g)

gui = GameGUI(800, 600, boggle.g)
gui.start()

while dpg.is_dearpygui_running():
    gui.run()