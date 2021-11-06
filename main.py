from flask import Flask, request, jsonify
from clean_data import consolidate_hotels
import config

app = Flask(__name__)

@app.route('/retrieve_hotels', methods=['GET'])
def retrieve_hotels():
    return jsonify(consolidate_hotels()),200

@app.route('/clear_hotel_cache', methods=['GET'])
def clear_hotel_cache():
    config.cache = {}
    return jsonify({"message": "cache cleared"}),200


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)