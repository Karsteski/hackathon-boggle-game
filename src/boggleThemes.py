import dearpygui.dearpygui as dpg

#Printing menu responses on console to verifing if it's working.
def print_me(sender):
    print(f"Menu item: {sender}")

#Button theme one, for alphabets used in Boggle game.
def set_button_theme_One(buttonId, themeId, r, g, b):
    with dpg.theme(id=themeId):
        """
        -Giving color to buttons
        -Frame Padding and increasing size of buttons
        -Frame Rounding for more styling
        """
        dpg.add_theme_color(dpg.mvThemeCol_Button, (r, g, b), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10, category=dpg.mvThemeCat_Core)  
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    #Linking theme id with button id
    dpg.set_item_theme(buttonId, themeId)

#Button theme two, for main operations in Boggle game
def set_button_theme_Two(buttonId, themeId, r, g, b):
    with dpg.theme(id=themeId):
        """
        -Giving color to buttons
        -Frame Rounding for styling
        """
        dpg.add_theme_color(dpg.mvThemeCol_Button, (r, g, b), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 7, category=dpg.mvThemeCat_Core)    
    
    #Linking theme id to button id
    dpg.set_item_theme(buttonId, themeId)

def open_file():
    dpg.file_dialog(default_filename="sample.txt")


#Primary window Main Menu Bar
""" TREE
-Options
|---Open File
|---Settings 
   |---Increase Font
   |---Decrease Font
-Help
|---About
|---Git Repo
"""

def add_menu():
    with dpg.menu_bar():
        with dpg.menu(label="Options"):
            dpg.add_menu_item(label="Open FIle", callback=open_file)

            with dpg.menu(label="settings"):
                dpg.add_menu_item(label="Increase Font", callback=print_me)
                dpg.add_menu_item(label="Decrease Font", callback=print_me)

        with dpg.menu(label="Help"):
            dpg.add_menu_item(label="About", callback=print_me)
            dpg.add_menu_item(label="Git repo", callback=print_me)
