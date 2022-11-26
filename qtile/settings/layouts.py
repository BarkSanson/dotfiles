from libqtile import layout

from .themes import colors

def init_layout_theme():
    return {
            "margin":7,
            "border_width":2,
            "border_focus": colors["highlight"],
            "border_normal": colors["inactive"]
            }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Matrix(**layout_theme),
]
