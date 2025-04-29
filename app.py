
from flask import Flask, jsonify
import myfitnesspal
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return 'MyFitnessPal API is running!'

@app.route('/mfp')
def get_mfp_data():
    try:
        client = myfitnesspal.Client('nevergo0604205', password='310700Vlad310700')
        today = datetime.today().date()
        day = client.get_date(today.year, today.month, today.day)

        data = {
            'date': str(today),
            'calories': day.totals.get('calories', 0),
            'carbohydrates': day.totals.get('carbohydrates', 0),
            'fat': day.totals.get('fat', 0),
            'protein': day.totals.get('protein', 0),
            'weight': day.measures.get('Weight', 'N/A')
        }

        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
