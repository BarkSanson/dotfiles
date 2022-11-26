import os
from libqtile import widget

from .themes import colors

home = os.path.expanduser('~')

def init_widgets_defaults():
    return dict(font="JetbrainsMono")

widget_defaults = init_widgets_defaults()

def separator():
    return widget.Sep(
        linewidth = 0,
        padding = 10,
        background = colors["background"]
    )

def powerline(
        padding: int = 3,
        foreground: str = colors["foreground"],
        background: str = colors["background"],
        fontsize: int = 15,
        left: bool = True):
    return widget.TextBox(
        font="JetbrainsMono",
        text="" if left else "",
        foreground=foreground,
        background=background,
        padding = padding,
        fontsize=fontsize
    )

def icon(
        padding: int = 3,
        foreground: str = colors["foreground"],
        background: str = colors["background"],
        fontsize: int = 15, 
        font:str = "JetbrainsMono",
        text: str = "?"):
    return widget.TextBox(
        font=font,
        text=text,
        foreground=foreground,
        background=background,
        padding=padding,
        fontsize=fontsize
    )

def workspaces():
    return widget.GroupBox(
        **init_widgets_defaults(),
        background=colors["background"],
        padding_x = 18,
        disable_drag = True,
        active = colors["active"],
        inactive = colors["inactive"],
        rounded = False,
        borderwidth=3,
        highlight_method = "line",
        highlight_color=colors["background"],
        this_current_screen_border=colors["highlight"],
        this_screen_border=colors["highlight"],
        other_current_screen_border=colors["background"],
        other_screen_border=colors["background"],
        urgent_alert_method='line',
        urgent_border=colors["urgent"],
        fontsize=18
        )

def systray(background: str = colors["background"]):
    return widget.Systray(
        **init_widgets_defaults(),
        background=background,
        icon_size=25,
        padding = 4,
        )

def current_layout(background: str = colors["background"]): 
    return widget.CurrentLayout(
        **init_widgets_defaults(),
        background=background,
        fontsize=15
        )

def window_name():
    return widget.WindowName(
        **init_widgets_defaults(),
        background=colors["background"],
        fontsize = 15,
        max_chars=30
        )

def battery(background: str = colors["background"]): 
    return widget.Battery(
        **init_widgets_defaults(),
        background=background,
        full_char="",
        charge_char="",
        discharge_char="",
        empty_char="ﳠ",
        notify_below=20,
        format='{char} {percent:2.0%}',
        fontsize=15,
        update_interval=10
    )

def cpu(background: str = colors["background"]):
    return widget.CPU(
        **init_widgets_defaults(),
        background=background,
        fontsize = 15
    )

def datetime(background: str = colors["background"]):
    return widget.Clock(
        **init_widgets_defaults(),
        background=background,
        fontsize = 15,
        format="%d/%m/%Y @ %H:%M"
    )

def secondary_widget_list():
    widgets_list = [
        icon(
            background=colors["foreground"],
            foreground=colors["background"],
            padding=15, 
            text="", 
            fontsize=30),
        powerline(
            padding=0, 
            fontsize=30,
            left=False),
        workspaces(),
        separator(),
        separator(),
        window_name(),
        powerline(
            foreground=colors["color1"],
            padding=0, 
            fontsize=30),
        icon(
            background=colors["color1"],
            text="",
            fontsize=18
            ),
        current_layout(colors["color1"]),
        powerline(
            background=colors["color1"],
            foreground=colors["color2"],
            padding=0,
            fontsize=30),
        icon(
            fontsize=18, 
            text="",
            background=colors["color2"]),
        cpu(colors["color2"]),
        powerline(
            background=colors["color2"],
            foreground=colors["color3"],
            padding=0,
            fontsize=30),
        icon(
            background=colors["color3"], 
            text=""),
        datetime(background=colors["color3"]),
        powerline(
            background=colors["color3"],
            foreground=colors["color4"],
            padding=0,
            fontsize=30),
        icon(
            background=colors["color4"], 
            text=""),
        battery(),
    ]
    return widgets_list

def main_widget_list():
    widgets_list = [
        *secondary_widget_list(),
        powerline(
            background=colors["color4"],
            foreground=colors["color5"],
            padding=0,
            fontsize=30),
        systray(colors["color5"])
    ]
    
    return widgets_list
