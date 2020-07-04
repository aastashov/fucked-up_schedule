# fucked-up_schedule
Simple web application to display COVID-19 charts for KGZ. We use the
 [Coronavirus Source Data](https://ourworldindata.org/coronavirus-source-data) for data getting and
 [Chart.js](https://www.chartjs.org/) for creating beautiful charts. 

## For developers
- We use [flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) like web server.
- [.editorconfig](https://editorconfig.org/)

```shell script
# install python specific version
pyenv install 3.8.0

# install pipenv (package manager)
pip install pipenv

# install deps and env
pipenv install

# start Web server
make runserver

# start parsing data
make runimporter
```
