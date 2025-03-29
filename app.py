from flask import Flask, jsonify, render_template
import requests
from models import db, Country  # No circular import
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

def fetch_and_store_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for country in data:
            name = country.get("name", {})
            common_name = name.get("common") if isinstance(name, dict) else "Unknown"
            population = country.get("population", 0)
            region = country.get("region", "Unknown")

            if common_name and not Country.query.filter_by(name=common_name).first():
                new_country = Country(name=common_name, population=population, region=region)
                db.session.add(new_country)

        db.session.commit()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    country_list = [{"name": c.name, "population": c.population, "region": c.region} for c in countries]
    return jsonify(country_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        fetch_and_store_countries()
    app.run(debug=True)


