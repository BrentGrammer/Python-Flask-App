## FLASK PROJECT

- Learning project

### Setup For Development

1. Create a virtual Env

   - `conda create -n myenvname python=3.7` in an Anaconda prompt
   - Activate the virtual Environment:
     - If using Anaconda, in windows, leave out `conda` in the command to activate in bash shell: `activate [myvenv]`

1. Install Flask: `pip install flask`

#### There are two ways to get things set up to run the app:

1. Set a FLASK_APP environment variable to your flask app entry point py file:

   - In the folder where you have your flask app python files, run `export FLASK_APP=myFlaskEntryFile.py`
   - (use `set FLASK_APP`... if in a windows terminal) **NOTE** You cannot name the entry point file `flask.py`
   - Run `export FLASK_DEBUG=1` to set hot reloading the server on updates in development

1. In your entry point file, add a debug argument set to true:

   ```python
   from flask import Flask
   app = Flask(__name__) # global variable == module name
   # the name will be __main__ if module is run directly with Python - this is done to eliminate having to set environment variables and use flask run, now we can just do `python flaskapp.py`
   if __name__ == '__main__':
     app.run(debug=True)
   ```

### Running the App in Development

- `flask run` to start serving the app on a local server
  ##### Or if you are not using environment variables set in the shell:
- `python [entrypoint.py]`

### Creating a Package to Simplify imports

- Making your app in a python package will make avoiding circular importing errors easier

1. Create a folder with the name of your app
1. Create a `__init__.py` file to make a python package
1. Move imports for Flask or creating a database etc. into `__init__.py`
1. Create a `routes.py` file in the package folder and move all routing code to that file
1. Rename your entry point file to `run.py` to avoid confusion/conflict with the package name. This file will only run the flask app.
1. Now you can run the app with `python run.py`

### Gotchas/Tips/Notes

- autoPep8 formatter for VSCode will not allow moving imports lower in the file - you can turn this off by going into the settings (`CTRL/CMD-,`) and adding an argument to autopep8Args: `--ignore=E402`

#### return JSON From Flask:

```python
from flask import jsonify

@app.route('/summary')
def summary():
    my_dict = { ... }
    return jsonify(my_dict)
```

#### Route Params:

- can optionally annotate the data type of the route param with `<datatype:param>` otherwise just use `<paramname>`

```python
@app.route('/post/<int:post_id>')
def post(post_id):
    # fetch post by id using route param variable passed in
    return my_post
```

#### Accetping POST and GET requests on a route:

```python
@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    # fetch post by id using route param variable passed in
    return my_post
```

#### Getting posted JSON data from a request:

```python
from flask import Flask, request, jsonify

@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    print content['mytext']
    return jsonify({"uuid":uuid})
```
