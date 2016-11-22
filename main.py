from flask import Flask

# Let's create very simple Flask application
application = Flask(__name__)

@application.route("/")
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    application.run()