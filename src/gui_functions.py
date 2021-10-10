import dearpygui.dearpygui as dpg
import dearpygui.themes as dpgThemes
from boggleThemes import *

class GameGUI(object):
    """
    GUI for the game of Boggle
    """

    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_grid = [[], [], [], [], []]
    current_word = []
    next_grid    = [[], [], [], [], []]  # For reset grid

    def __init__(self, window_width, window_height, input_grid):
        dpgThemes.create_theme_imgui_light(default_theme=False)
        self.window_width = window_width
        self.window_height = window_height
        self.current_grid = input_grid
        self.viewport = dpg.create_viewport(title="Hackathon Game - Boggle", width=window_width, height=window_height)

    def grid_button_callback(self, sender, data):
        self.current_word.append(dpg.get_item_label(sender))

    # Reset current word
    def new_word_callback(self, sender, data):
        self.current_word.clear()

    # Reset grid.
    def reset_button_callback(self, sender, data):
        self.current_grid = self.next_grid

    def save_word_callback(self):
        self.current_word.clear()

    def start(self):
        dpg.setup_dearpygui(viewport=self.viewport)

        with dpg.window(id="Primary Window", label="Example-Window"):
            # Create button grid
            n = 0  # For grid layout
            #Adding menu to the primary window.
            add_menu()
            for outer_grid in self.current_grid:
                for inner_grid in outer_grid:
                    dpg.add_button(
                        label=inner_grid, id=(str(inner_grid) + str(n)), callback=self.grid_button_callback
                    )  # The id is just meant to be unique
                    set_button_theme_One(
                        (str(inner_grid) + str(n)), inner_grid, 23, 140, 255
                        )
                    if n < 4:
                        dpg.add_same_line()
                    if n >= 4:
                        n = 0
                    else:
                        n += 1

            # Game Function Buttons
            dpg.add_same_line(spacing=20)
            dpg.add_spacing(count=3)
            dpg.add_button(id="reset", label="Reset", callback=self.reset_button_callback)
            dpg.add_same_line(spacing=10)
            dpg.add_button(id="new_word", label="New Word", callback=self.new_word_callback)
            dpg.add_same_line(spacing=10)
            dpg.add_button(id="save_word", label="Save Word", callback=self.save_word_callback)

            dpg.set_primary_window("Primary Window", True)  # So that window fills the entire viewport
            dpg.show_viewport(self.viewport)

            # Display current word
            dpg.add_text(self.current_word, id="current_word")
            
        #Orange themed functions button
        set_button_theme_Two("reset", "theme_1", 255, 140, 23)      
        set_button_theme_Two("new_word", "theme_2", 255, 140, 23)  
        set_button_theme_Two("save_word", "theme_3", 255, 140, 23)

    def run(self):
        dpg.render_dearpygui_frame()

        # Change displayed word
        dpg.set_value(item="current_word", value=self.current_word)

        # Change displayed grid
        # Need to iterate over the grid buttons and reset them somehow... Might be a headache *_*

    def exit(self):
        dpg.cleanup_dearpygui()
