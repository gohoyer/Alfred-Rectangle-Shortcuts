#!/usr/bin/env python3
#
# This scrit read a Rectangle Config File (exported as json)
# and output the  shortcuts on script filter format for Alfred.
# https://www.alfredapp.com/help/workflows/inputs/script-filter/json/

import json
import sys
import os

# JSON file
config_file = open(os.environ['RECT_CONFIG_FILE'], "r")

# Reading from file
data = json.loads(config_file.read())

# Iterating through the json
# list

formatted_results = []

if len(data) == 0:
    result = {
        "title": "No shortcuts found.",
        "subtitle": "Please make sure you have exported Rectangle JSON and informed the right path for it.",
    }
    formatted_results.append(result)
else:
    for shortcut in data['shortcuts']:
        result = {
            "title": shortcut,
            "subtitle": "Move/snap the window to " + shortcut + ".",
            "arg": str(data['shortcuts'][shortcut]['keyCode']) + "#with#" + str(data['shortcuts'][shortcut]['modifierFlags']),
            "autocomplete": shortcut,
            "icon": {
                "path": "./images/" + shortcut + ".png"
            }
        }
        formatted_results.append(result)

# Return the avaliable arrangements on alfred joson format
alfred_json = json.dumps({"items": formatted_results}, indent=2)
sys.stdout.write(alfred_json)

# Closing file
config_file.close()
