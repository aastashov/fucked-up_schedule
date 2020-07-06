from flask import Flask, render_template

from application.settings import STATIC
from application.storage import storage

app = Flask(__name__, static_url_path=STATIC)


@app.route('/')
def hello_world():
    storage_dataset = storage.load_data()

    labels = []
    datasets = {}
    for label, dataset in storage_dataset.items():
        labels.append(label)
        for name, data in dataset.items():
            d = datasets.get(name) or None
            if d is None:
                d = data
                d['data'] = [d['value']]
                d['name'] = name
            else:
                d['data'].append(data['value'])
            datasets[name] = d

    return render_template('index.html', **{
        'country': 'Kyrgyzstan',
        'labels': labels,
        'dataset': list(datasets.values()),
    })
