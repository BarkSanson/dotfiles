from libqtile import bar
from libqtile.config import Screen

from .widgets import main_widget_list, secondary_widget_list
from .themes import colors

def init_widgets_screen1():
    widgets_screen1 = main_widget_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = secondary_widget_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()

def status_bar(widgets):
    return bar.Bar(
            widgets, 
            size=30, 
            opacity=1, 
            border_width=0,
            margin=7,
            border_color=[
                "#000000", 
                colors["color4"], 
                "#000000", 
                colors["foreground"]])

def init_screens():
    return [Screen(top=status_bar(init_widgets_screen1())),
            Screen(top=status_bar(init_widgets_screen2()))]

screens = init_screens()
