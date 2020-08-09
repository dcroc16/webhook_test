from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')



@app.route("/data/<name>/<age>/<weight>")
def data_get_name(name='default', age=0, weight=24):
    return jsonify([name, age, weight])




