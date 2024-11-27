import webbrowser

from flask import Flask, render_template
import webview

app: Flask = Flask(__name__, static_folder='assets', template_folder='templates')


def handle_external_websites(url):
    """
    What is this used for?\n
    Markdown files might contain urls that lead you to external website.
    In PyWebView, these websites open in webview itself instead of opening the user's default browser.
    So, now it opens external url or websites in user's default browser.
    :arg url The external url. For example, 'example.com' or 'google.com'
    :return False
    """
    webbrowser.open(url)
    return False


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # noinspection PyTypeChecker
    webview.create_window("Markdown Reader and Editor", app, js_api={'handle_url': handle_external_websites})
    webview.start()
