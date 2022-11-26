import json
import os

home = os.path.expanduser('~')

root = os.path.join(home, ".config", "qtile")
themes_folder = os.path.join(root, "themes")

with open(os.path.join(themes_folder, 'winter-is-coming.json'), 'r') as data:
    theme = json.load(data)

print(theme)
