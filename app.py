from flask import Flask, jsonify, render_template
from helpers.HousingData import statcan_data, csv_to_json
from helpers.FoodBankData import food_bank_data

app = Flask(__name__)

PROJECTS_PATH = "data/download_data.csv"
FOODBANK_PATH = "data/foodbanks_ATLANTIC.csv"


@app.route("/")
def index():
    statcan_data()
    return render_template("index.html")


@app.route("/api/test")
def test():
    return jsonify({"msg": "Hello"})


@app.route("/api/get-data")
def send_data():
    final_json = {}
    final_json["projects"] = csv_to_json(PROJECTS_PATH)['projects']
    final_json["food_banks"] = food_bank_data(FOODBANK_PATH)['food_banks']
    return jsonify(final_json)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
