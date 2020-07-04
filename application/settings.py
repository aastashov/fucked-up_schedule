import os
import pathlib

BASE_PATH = os.path.dirname(pathlib.Path(__file__).parent.absolute())

DATA_URL = 'https://covid.ourworldindata.org/data/owid-covid-data.json'

STATIC = os.path.join(BASE_PATH, 'static/')

# directory for store data
DATA_DIR = os.path.join(BASE_PATH, 'dist')
LOCAL_DATA_FILE = os.path.join(DATA_DIR, 'data.json')
