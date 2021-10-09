import dearpygui.dearpygui as dpg

class GameGUI(object):
    """
    GUI for the game of Boggle
    """

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.viewport = dpg.create_viewport(title="Hackathon Game - Boggle", width=window_width, height=window_height)

    def start(self):
        dpg.setup_dearpygui(viewport=self.viewport)

        with dpg.window(id="Primary Window", label="Example-Window"):
            dpg.add_button(label="moo")
        
        dpg.set_primary_window("Primary Window", True) # So that window fills the entire viewport

        dpg.show_viewport(self.viewport)

    def run(self):
        dpg.render_dearpygui_frame()

    def exit(self):
        dpg.cleanup_dearpygui()

    # def get_clicked_positions(self):

    # def reset_word(self):

    # def set_word(self):
