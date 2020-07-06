""" importer should download the open data, parse countries and put data to storage """
from typing import Dict

import requests

from application.settings import DATASET_URLS
from application.storage import storage


def owid_parser() -> Dict:
    dataset = _make_request(DATASET_URLS['owid'])
    result_dataset = {}

    for data in dataset['KGZ']['data']:
        """
        {'date': '2020-03-19',
         'total_cases': 3.0,
         'new_cases': 3.0,
         'total_deaths': 0.0,
         'new_deaths': 0.0,
         'total_cases_per_million': 0.46,
         'new_cases_per_million': 0.46,
         'total_deaths_per_million': 0.0,
         'new_deaths_per_million': 0.0,
         'stringency_index': 63.89}
        """
        key = data['date']
        dataset = result_dataset.get(key) or {}
        dataset['new_cases'] = {
            'en': 'New cases',
            'ru': 'Новые случаи',
            'value': int(data['new_cases']),
        }

        dataset['new_deaths'] = {
            'en': 'New deaths',
            'ru': 'Новых смертей',
            'value': int(data['new_deaths']),
        }
        result_dataset[key] = dataset
    return result_dataset


def ecdc_parser() -> Dict:
    dataset = _make_request(DATASET_URLS['ecdc'])
    result_dataset = {}
    for data in dataset['records']:
        if data['countryterritoryCode'] == 'KGZ':
            """
            {'dateRep': '25/03/2020',
            'day': '25',
            'month': '03',
            'year': '2020',
            'cases': 26,
            'deaths': 0,
            'countriesAndTerritories': 'Kyrgyzstan',
            'geoId': 'KG',
            'countryterritoryCode': 'KGZ',
            'popData2019': 6415851,
            'continentExp': 'Asia'}
            """
            key = f'{data["year"]}-{data["month"]}-{data["day"]}'
            dataset = result_dataset.get(key) or {}
            dataset['new_cases'] = {
                'en': 'New cases',
                'ru': 'Новые случаи',
                'value': data['cases'],
            }

            dataset['new_deaths'] = {
                'en': 'New deaths',
                'ru': 'Новых смертей',
                'value': data['deaths'],
            }
            result_dataset[key] = dataset
    return result_dataset


def _make_request(target: str) -> Dict:
    response = requests.get(target)
    response.raise_for_status()

    print('Receive data')
    response_json = response.json()
    return response_json


if __name__ == '__main__':
    kgz_data = owid_parser()
    # kgz_data = ecdc_parser()
    storage.write_data(kgz_data)
    print('Write data to storage!')
