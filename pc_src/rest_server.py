from flask import Flask, jsonify, render_template, url_for, request
from flask_googlecharts import GoogleCharts, MaterialLineChart
import json

from charta_data import example_data



app = Flask(__name__)
charts = GoogleCharts(app)


@app.route("/data")
def data():
    d = example_data()
    return jsonify(d)

@app.route("/")
def index():
    wykres = MaterialLineChart("wykres", options={"title": "Wykres1", "width": 500, "height": 300}, data_url=url_for('data'))
    charts.register(wykres)
    return render_template("index.html")


@app.route('/servo', methods=['POST'])
def servo():
    if not request.json:
        print('Error')
    print(request.data)
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
    print(request.data)
	#tutaj trzeba zapisac otrzymana dane do pliku do wykresu
    return json.dumps(request.json)
 
    
if __name__ == "__main__":
    app.run(debug=True)
