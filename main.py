from flask import Flask, request, jsonify
import json
import requests
from clean_data import consolidate_hotels

app = Flask(__name__)

@app.route('/retrieve_hotels', methods=['GET'])
def retrieve_hotels():
    return jsonify(consolidate_hotels()),200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)