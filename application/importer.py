""" importer should download the open data, parse countries and put data to storage """
import requests

from application.settings import DATA_URL
from application.storage import storage


def parse():
    response = requests.get(DATA_URL)
    response.raise_for_status()

    print('Receive data')
    response_json = response.json()
    kgz_data = response_json['KGZ']
    storage.write_data(kgz_data)
    print('Write data to storage!')


if __name__ == '__main__':
    parse()
