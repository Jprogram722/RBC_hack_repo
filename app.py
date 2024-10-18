from flask import Flask, jsonify, render_template
from helpers.convertToJson import csv_to_json
from helpers.getHousingData import get_data

app = Flask(__name__)

FILE_PATH = "data/download_data.csv"


@app.route("/")
def new_test():
    get_data()
    return render_template("index.html")


@app.route("/api/test")
def test():
    return jsonify({"msg": "Hello"})


@app.route("/api/get-data")
def get_data():
    return jsonify(csv_to_json(FILE_PATH))


if __name__ == "__main__":
    app.run()
