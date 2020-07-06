import os
import pathlib

BASE_PATH = pathlib.Path(__file__).parent.absolute()

DATASET_URLS = {
    'ecdc': 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json',
    'owid': 'https://covid.ourworldindata.org/data/owid-covid-data.json',
}

STATIC = os.path.join(BASE_PATH, 'static/')

# directory for store data
DATA_DIR = os.path.join(BASE_PATH, 'dist')
LOCAL_DATA_FILE = os.path.join(DATA_DIR, 'data.json')
