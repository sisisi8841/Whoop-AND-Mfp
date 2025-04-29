
from flask import Flask, request, jsonify
from mfp import MyFitnessPalClient
from notion_utils import write_to_notion

app = Flask(__name__)

@app.route('/pull-mfp-data', methods=['GET'])
def pull_mfp_data():
    username = 'nevergo0604205'
    password = '310700Vlad310700'

    try:
        mfp = MyFitnessPalClient(username, password)
        data = mfp.get_day_summary()  # Отримати дані за сьогодні
        notion_response = write_to_notion(data)
        return jsonify({'status': 'success', 'notion': notion_response})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
