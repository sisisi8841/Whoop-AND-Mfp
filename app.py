import myfitnesspal
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Whoop + MFP server is running!"

@app.route("/mfp")
def get_mfp_data():
    client = myfitnesspal.Client("nevergo0604205", "310700Vlad310700")
    day = client.get_date()
    summary = {
        "calories": day.totals.get("calories", 0),
        "carbohydrates": day.totals.get("carbohydrates", 0),
        "fat": day.totals.get("fat", 0),
        "protein": day.totals.get("protein", 0),
        "sodium": day.totals.get("sodium", 0),
        "sugar": day.totals.get("sugar", 0),
        "water": day.water,
    }
    return jsonify(summary)
