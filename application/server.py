from flask import Flask, render_template

from application.storage import storage
from application.settings import STATIC

app = Flask(__name__, static_url_path=STATIC)


@app.route('/')
def hello_world():
    dataset = storage.load_data()

    labels = [i['date'] for i in dataset['data']]
    raw_data = [int(i['new_cases']) for i in dataset['data']]

    context = {
        'dataset': dataset,
        'label': 'Новые случаи',
        'labels': labels,
        'raw_data': raw_data,
    }
    return render_template('index.html', **context)
