from flask import Flask, jsonify, render_template, url_for, request
from flask_googlecharts import GoogleCharts, MaterialLineChart
import json

app = Flask(__name__)
charts = GoogleCharts(app)


@app.route("/data")
def data():
    with open('chart_data.json') as f:
        d = json.loads(f.read())

    return jsonify(d)


@app.route("/")
def index():
    wykres = MaterialLineChart("wykres", options={"title": "Chart 1", "width": 500, "height": 300}, data_url=url_for('data'))
    charts.register(wykres)
    return render_template("index.html")


@app.route('/servo', methods=['POST'])
def servo():
    if not request.json:
        print('Error')
    with open('pozycja_zadana.json', 'w') as f:
        json.dump(request.json, f)
    return json.dumps(request.json)


@app.route('/pozycja_zadana', methods=['GET'])
def pozycja_zadana():
    f = open('pozycja_zadana.json', 'r')
    d = f.read()
    return jsonify(d)


@app.route('/pozycja_aktualna', methods=['POST'])
def pozycja_aktualna():
    if not request.json:
        print('Error')
    payload = json.loads(request.data)
    actual_position = int(payload.get('pozycja'))
    save_servo_data(position=actual_position)
    return json.dumps(request.json)


def save_servo_data(position: int):
    with open('chart_data.json') as f:
        d = json.loads(f.read())
    actual_data = d
    data_length = len(actual_data.get('rows'))
    new_row = {"c": [{"v": data_length, "f": None}, {"v": position, "f": None}]}
    actual_data['rows'].append(new_row)
    with open('chart_data.json', 'w') as f:
        json.dump(actual_data, f)


if __name__ == "__main__":
    app.run(debug=True)
