"""
Made by Mithun
Markdown Reader and Writer
Version - 0.2
"""


import json

from flask import Flask, render_template, redirect
import webview
import argparse

app: Flask = Flask(__name__, static_folder='assets', template_folder='templates')

VERSION: str = "0.0.1"

def get_dark_mode():
    with open("config.json", 'r') as file:
        data = json.load(file)
        tmp = data["darkMode"]
        file.close()
    return tmp

def change_mode(mode: bool) -> None:
    """
    Changes the dark_mode value in 'config.json'
    :param mode: If dark mode then true else false
    :return: None
    """

    # Open and load the JSON file, modify the "darkMode" field
    with open("config.json", 'a+') as file:
        data = json.load(file)
        data["darkMode"] = mode

    # Write the updated data back to the JSON file
    with open("config.json", 'w') as file1:
        json.dump(file1, data)
    file1.close()


@app.route("/")
def index():
    return redirect("/reader")

@app.route("/reader")
def reader():
    return render_template("index.html", dm=get_dark_mode())

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/togglelightmode")
def togglelightmode():
    change_mode(False)
    return render_template("settings.html", dm=get_dark_mode())
@app.route("/toggledarkmode")
def toggledarkmode():
    change_mode(True)
    return render_template("settings.html", dm=get_dark_mode())




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Markdown Reader and Writer options")
    parser.add_argument("-help", help="Options:\n\n1: -file 'f.md' - to open a file\n\nMade by Mithun. Version: " + VERSION)
    parser.add_argument("-file", type=str, help="Example: 'filename.md' or 'README.md'")
    args = parser.parse_args()
    if args.help:
        print("Options:\n\n1: -file 'f.md' - to open a file\n\nMade by Mithun. Version: " + VERSION)
        exit()
    elif args.file:
        webview.create_window("Markdown Reader and Editor", app)
        webview.start(args="file")
        
    webview.settings = {
        'ALLOW_DOWNLOADS': True,
        'ALLOW_FILE_URLS': False,
        'OPEN_EXTERNAL_LINKS_IN_BROWSER':True,
        'OPEN_DEVTOOLS_IN_DEBUG': True,
    }

    webview.create_window("Markdown Reader and Editor", app)
    webview.start(debug=False)
