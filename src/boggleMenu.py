import dearpygui.dearpygui as dpg

#Printing menu responses on console to verifing if it's working.
def print_me(sender):
    print(f"Menu item: {sender}")

#Menu->Help->About
def help_about():
    with dpg.window(id="help_about_window", label="About", modal=True):
        dpg.add_text(
            """
            Version 1.0.1 Oct 10, 2021
            A Fun Boggle Game created by 
            -github/AndrewWigginCout
            -github/Karsteski
            -github/Ved9rakash

            as a project of MakeUC 2021 hackathon, University Of Cincinati
            """
        )
        
#Menu->Help->Git repo
def git_repo():
    with dpg.window(id="git_about_window", label="Github Reporsitory", modal=True):
        dpg.add_text("https://github.com/Karsteski/hackathon-boggle-game")

def open_file():
    dpg.file_dialog(default_filename="sample.txt")

def add_menu():
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
    with dpg.menu_bar():
        with dpg.menu(label="Options"):
            dpg.add_menu_item(label="Open FIle", callback=open_file)

            with dpg.menu(label="settings"):
                dpg.add_menu_item(label="Increase Font", callback=print_me)
                dpg.add_menu_item(label="Decrease Font", callback=print_me)

        with dpg.menu(label="Help"):
            dpg.add_menu_item(label="About", callback=help_about)
            dpg.add_menu_item(label="Git repo", callback=git_repo)
