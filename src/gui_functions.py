import dearpygui.dearpygui as dpg
import dearpygui.themes as dpgThemes
from boggleThemes import *
from boggleMenu import *

def print_value(sender):
    print(dpg.get_value(sender))
class GameGUI(object):
    """
    GUI for the game of Boggle
    """

    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_word = []
    next_grid    = [[], [], [], [], []]  # For reset grid

    def __init__(self, window_width, window_height, input_grid):
        dpgThemes.create_theme_imgui_light(default_theme=False)
        self.window_width = window_width
        self.window_height = window_height
        self.current_grid = input_grid
        self.viewport = dpg.create_viewport(title="Hackathon Game - Boggle", width=window_width, height=window_height)
        self.appfont="../resources/lucon.ttf"
    def grid_button_callback(self, sender, data):
        print_value(sender)
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

        with dpg.font_registry():
            dpg.add_font(self.appfont, 50, default_font=True)

        with dpg.window(id="Primary Window", label="Example-Window"):
            # Create button grid
            n = 0  # For grid layout
            #Adding menu to the primary window.
            add_menu()
            M,N = 5,5
            y_margin,x_margin=60,60
            for j in range(M):
                for i in range(N):
                    id=dpg.add_button(
                        label=self.current_grid[j][i],
                        id=200+j*5+i,
                        pos=(x_margin+i*100,y_margin+j*100),
                        callback=self.grid_button_callback,
                        width=100,
                        height=100,
                    ) 
                    print(id)
                    # The id is just meant to be unique
                    # set_button_theme_One(
                       # str(j*5+i),
                       # "One",
                       # 23, 140, 255
                       # )
            
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
