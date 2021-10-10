import dearpygui.dearpygui as dpg


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