## FLASK PROJECT

- Learning project

### Setup For Development

- Create a virtual Env

  - In windows bash, leave out `conda` in the command: `activate [myvenv]`

- Set a FLASK_APP environment variable to your flask app entry point py file:

  - In the folder where you have your flask app python files, run `export FLASK_APP=myFlaskEntryFile.py`
  - **NOTE** You cannot name the entry point file `flask.py`

- Run `flask run` to start serving the app on a local server
