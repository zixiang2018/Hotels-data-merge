from flask import Flask, request, jsonify
from clean_data import consolidate_hotels
import config
import json

app = Flask(__name__)

@app.route('/api/retrieve_all_hotels', methods=['GET'])
def retrieve_hotels():
    return jsonify(consolidate_hotels()),200

@app.route('/api/clear_hotel_cache', methods=['GET'])
def clear_hotel_cache():
    config.cache = {}
    return jsonify({"message": "cache cleared"}),200

@app.route('/api/retrieve_hotels_by_ids', methods=['POST'])
def retrieve_hotels_by_ids():
    result = []
    requested_hotels = json.loads(request.data)
    hotels = consolidate_hotels()
    for hotel in hotels:
        if hotel["id"] in requested_hotels["hotel_ids"]:
            result.append(hotel)
    return jsonify(result),200

@app.route('/api/retrieve_hotels_by_destinations', methods=['POST'])
def retrieve_hotels_by_destinations():
    result = []
    requested_dest = json.loads(request.data)
    hotels = consolidate_hotels()
    for hotel in hotels:
        if hotel["destination_id"] in requested_dest["destination_ids"]:
            result.append(hotel)
    return jsonify(result),200

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)