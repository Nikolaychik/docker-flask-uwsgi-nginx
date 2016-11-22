from flask import Flask
from flask import render_template


# let's make our simple Flask application a bit more interesting!
application = Flask(__name__)

@application.route("/")
def index():
    return 'Hello World!'


if __name__ == '__main__':
    application.run()