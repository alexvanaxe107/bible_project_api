# Welcome to Bible Project api documentation

Here is all technical information needed for the bible api project.

## Technology


* [Fastapi](https://fastapi.tiangolo.com/) - The framework used to provide the rest api funcionality.
* [SQLAlchemy](https://www.sqlalchemy.org/) - The tool to interact with the database. (An ORM)
* uvicorn - Used to provide the development server


## Project layout

The actual project is inside the app directory.

    api/                       # The root of the project
    ├── app/                   # The application files
    ├── modules/               # The submodules of the application
    │   └── bible.py           # The core of the bible project. Here we retrieve the word.
    ├── sql/                   # The database related files
    │   ├── database.py        # The sqlalchemy database connection
    │   ├── models.py          # The sqlalchemy models
    │   ├── schemas.py         # It's the pydantic models, used to return the data and get it by fast
    │   └── crud.py            # The queries using the sqlalchemy
    ├── data/                  # The database files
    ├── flake.nix              # The project dependencies for who work in nixos
    ├── requirements.in        # The input for the pip-tools to manage the python dependencies
    ├── requirements.txt       # The compiled dependencies of the project
    └── shell.nix              # The development enviromnent used in nixos
