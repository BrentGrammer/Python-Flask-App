from flask import Flask
app = Flask(__name__)  # global variable == module name

# modules from the package depending on the app variable must be imported after it is created:
from flaskapp import routes
