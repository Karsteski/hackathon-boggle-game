import dearpygui.dearpygui as dpg
import random


class GameGUI(object):
    """
    GUI for the game of Boggle
    """

    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    buttons = []
    current_word = []

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.viewport = dpg.create_viewport(title="Hackathon Game - Boggle", width=window_width, height=window_height)

    def button_callback(self, sender, data):
        self.current_word.append(dpg.get_item_label(sender))

    def start(self):
        dpg.setup_dearpygui(viewport=self.viewport)

        with dpg.window(id="Primary Window", label="Example-Window"):
            # Create button grid
            for x in range(5):
                for y in range(5):
                    dpg.add_button(
                        label=random.choice(self.LETTERS), id=(str(x) + str(y)), callback=self.button_callback
                    )
                    if y < 4:
                        dpg.add_same_line()

            # Game Function Buttons
            dpg.add_button(id="reset", label="Reset")
            dpg.add_same_line()
            dpg.add_button(id="new_word", label="New Word")
            dpg.add_same_line()
            dpg.add_button(id="set_word", label="Set Word")

            # Current Word
            dpg.add_text(self.current_word)

            dpg.set_primary_window("Primary Window", True)  # So that window fills the entire viewport
            dpg.show_viewport(self.viewport)

    def run(self):
        dpg.render_dearpygui_frame()

    def exit(self):
        dpg.cleanup_dearpygui()

    # def get_clicked_positions(self):

    # def reset_word(self):

    # def set_word(self):
