from gui_functions import *
from boggle_game import *


# Test Grid
test_grid = [["a", "f"], ["b", "g"], ["c", "h"], ["d", "i"], ["e", "j"]]

gui = GameGUI(800, 600, test_grid)
gui.start()

while dpg.is_dearpygui_running():
    gui.run()