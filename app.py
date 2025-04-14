from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from config import Config
from models import db, Country

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Fetch & store countries from REST API
def fetch_and_store_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        for country in data:
            name = country.get("name", {}).get("common", "N/A")
            population = country.get("population", 0)
            region = country.get("region", "N/A")
            capital = country.get("capital", ["N/A"])[0]
            flag_url = country.get("flags", {}).get("png", "")

            if not Country.query.filter_by(name=name).first():
                new_country = Country(
                    name=name,
                    population=population,
                    region=region,
                    capital=capital,
                    flag_url=flag_url
                )
                db.session.add(new_country)
        db.session.commit()

# Home route with search/filter
@app.route("/")
def home():
    search = request.args.get("search", "").lower()
    region = request.args.get("region", "")

    query = Country.query
    if search:
        query = query.filter(Country.name.ilike(f"%{search}%"))
    if region:
        query = query.filter(Country.region == region)

    countries = query.all()
    return render_template("index.html", countries=countries)

# API for chart or frontend JS
@app.route("/countries")
def get_countries():
    countries = Country.query.all()
    return jsonify([{
        "name": c.name,
        "capital": c.capital,
        "region": c.region,
        "population": c.population,
        "flag": c.flag_url
    } for c in countries])

# Data for Chart.js
@app.route("/chart-data")
def chart_data():
    regions = db.session.query(Country.region, db.func.sum(Country.population))\
                        .group_by(Country.region).all()
    return jsonify({
        "labels": [r[0] for r in regions],
        "values": [r[1] for r in regions]
    })

if __name__ == '__main__':
    with app.app_context():
        # Force recreate DB from model
        db.drop_all()
        db.create_all()
        fetch_and_store_countries()
    app.run(debug=True)

