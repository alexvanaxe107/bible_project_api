# Bible Project API

This is the BP API, here you will find instructions on how to setup the enviromnent and run the project.

## Install

The default setup is made to run on a nix os distro, using flake setup. So, the first thing to do is enter on the development shell:

```bash
nix develop
```

Probably you will see an error for the first time. It's ok. Now you need to create the python virtual envoromnent:
```bash
python -m venv .venv
```

After this, you will have installed postgrees and started it, and created the python enviromnent. Exit the shell and enter again to activate the python venv.
After that, you need to install the dependencies, for that we use pip-tools. So install pip-tools and synch the packages.

```bash
pip install pip-tools
pip-sync
```

Ok, you have everything installed.

# Configure the database

Next step is configure the database. A user 'alexvanaxe' is created in shell.nix, you can change to your name of liking and update the commands bellow. It is a good advice to create one with the same name of your linux user.
So we create the database and populate it.

```bash
createdb --host=localhost -O alexvanaxe bible_project
cd data
psql --host=localhost bible_project < ara.dump.sql
```

Congratulations! Everything is configured.

## Run

The app is a fast based app, we run it using uvicorn. To do so, just enter the app and start uvicorn.

```bash
uvicorn main:app --reload
```

Hopefully no error will occour.

You can access the page in your localhost at http://localhost:8000/docs and test some of it.
