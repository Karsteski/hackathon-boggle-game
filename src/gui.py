from gui_functions import *

from boggle_game import *

gui = GameGUI(800, 600)
gui.start()

while dpg.is_dearpygui_running():
    gui.run()
