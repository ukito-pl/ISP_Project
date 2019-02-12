from flask import Flask, jsonify, render_template, url_for
from flask_googlecharts import GoogleCharts, BarChart, MaterialLineChart
from flask_googlecharts.utils import prep_data

import datetime

app = Flask(__name__)
charts = GoogleCharts(app)


@app.route("/data")
def data():

    d = {"cols": [{"id": "", "label": "syf", "pattern": "", "type": "number"},
                  {"id": "", "label": "Spectators", "pattern": "", "type": "number"}],
         "rows": [{"c": [{"v": 1, "f": None}, {"v": 5, "f": None}]},
                  {"c": [{"v": 2, "f": None}, {"v": 6, "f": None}]},
                  {"c": [{"v": 3, "f": None}, {"v": 7, "f": None}]},
                  {"c": [{"v": 4, "f": None}, {"v": 8, "f": None}]},
                  {"c": [{"v": 5, "f": None}, {"v": 9, "f": None}]},
                  {"c": [{"v": 6, "f": None}, {"v": 10, "f": None}]}]}

    return jsonify(prep_data(d))


@app.route("/")
def index():
    spectators_chart = MaterialLineChart("spectators",
                                         options={"title": "Contest Spectators",
                                                  "width": 500,
                                                  "height": 300},
                                         data_url=url_for('data'))

    charts.register(spectators_chart)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
