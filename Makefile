runserver:
	export FLASK_APP=application/server.py && export FLASK_ENV=development && flask run

importer:
	export PYTHONPATH=. && python application/importer.py
