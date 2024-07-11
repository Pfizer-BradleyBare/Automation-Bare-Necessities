import os
import pathlib

database_file = pathlib.Path(__file__).parent / "db.sqlite3"
database_file.unlink(True)

for root, dirs, files in os.walk(pathlib.Path(__file__).parent):
    if "migrations" in root:
        for file in files:
            if ".py" in file and "__init__.py" not in file:
                (pathlib.Path(root) / file).unlink(True)
