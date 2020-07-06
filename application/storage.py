""" storage.py file need for work with a local storage """
from pathlib import Path
from typing import TYPE_CHECKING

from flask import json

from application.settings import LOCAL_DATA_FILE, DATA_DIR

if TYPE_CHECKING:
    from typing import Dict


class Storage:
    """
    I don't know how need a correctly work with wile. What should make this class?
    1. Open or Create file for save data
    2. Provide methods for write to file
    3. Correctly close file

    """
    _file = None
    _json = {}

    def __init__(self):
        self._load_file()

    def __del__(self):
        if self._file is not None:
            self._file.close()

    def _open_file(self):
        self._file = open(LOCAL_DATA_FILE, 'w+')

    def _load_file(self):
        Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
        try:
            with open(LOCAL_DATA_FILE, 'r+') as _file:
                self._json = json.load(_file)
        except FileNotFoundError:
            self._json = {}

    def _write_file(self):
        with open(LOCAL_DATA_FILE, 'w+') as _file:
            json.dump(self._json, _file)

    def load_data(self, fresh=False) -> 'Dict':
        if not fresh and self._json:
            return self._json
        self._load_file()

    def write_data(self, data: 'Dict'):
        """ Should receive
        {
            "2020-12-01": {
                "new_cases": {
                    "en": "New cases",
                    "ru": "Новые случаи",
                    "value": 32
                },
                "new_deaths": {
                    # ...
                }
            },
            "2020-12-02": [
                # ...
            ]
        }
        """
        self._json = data
        self._write_file()


storage = Storage()
