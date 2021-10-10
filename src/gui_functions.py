import dearpygui.dearpygui as dpg


class GameGUI(object):
    """
    GUI for the game of Boggle
    """

    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_grid = [[], [], [], [], []]
    current_word = []
    next_grid = [[], [], [], [], []]  # For reset grid

    def __init__(self, window_width, window_height, input_grid):
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

    def start(self):
        dpg.setup_dearpygui(viewport=self.viewport)

        with dpg.window(id="Primary Window", label="Example-Window"):
            # Create button grid
            n = 0  # For grid layout
            N,M = 5,5
            for j in range(M):
                for i in range(N):
                    dpg.add_button(
                        label=self.current_grid[j][i], id=(str(5*j+i)),
                        pos=(i*100,j*100),
                        callback=self.grid_button_callback
                    )  # The id is just meant to be unique



            # Game Function Buttons
            dpg.add_button(id="reset", label="Reset", callback=self.reset_button_callback)
            dpg.add_same_line()
            dpg.add_button(id="new_word", label="New Word", callback=self.new_word_callback)

            dpg.set_primary_window("Primary Window", True)  # So that window fills the entire viewport
            dpg.show_viewport(self.viewport)

            # Display current word
            dpg.add_text(self.current_word, id="current_word")

    def run(self):
        dpg.render_dearpygui_frame()

        # Change displayed word
        dpg.set_value(item="current_word", value=self.current_word)

        # Change displayed grid
        # Need to iterate over the grid buttons and reset them somehow... Might be a headache *_*

    def exit(self):
        dpg.cleanup_dearpygui()
