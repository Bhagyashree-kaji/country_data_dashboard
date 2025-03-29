from flask import Flask, jsonify
import requests

app = Flask(__name__)

def fetch_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

@app.route('/countries', methods=['GET'])
def get_countries():
    data = fetch_countries()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
