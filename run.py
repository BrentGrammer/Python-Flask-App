'''
    All this file does is run the flask app created from the package in flaskapp/__init__.py
'''

# import the package created to avoid circular import errors:
from flaskapp import app

# the name will not be __main__ if module is imported, only if run directly
if __name__ == '__main__':
    app.run(debug=True)
