import requests
from models import db, Country
from main import app

def fetch_and_store_countries():
    with app.app_context():
        db.drop_all()
        db.create_all()

        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)

        if response.status_code == 200:
            countries = response.json()
            for country in countries:
                try:
                    name = country.get("name", {}).get("common", "N/A")
                    capital = country.get("capital", ["N/A"])[0]
                    region = country.get("region", "N/A")
                    subregion = country.get("subregion", "N/A")
                    population = country.get("population", 0)
                    flag = country.get("flags", {}).get("png", "")

                    if name and not Country.query.filter_by(name=name).first():
                        c = Country(
                            name=name,
                            capital=capital,
                            region=region,
                            subregion=subregion,
                            population=population,
                            flag_url=flag
                        )
                        db.session.add(c)
                except Exception as e:
                    print(f"Error adding country: {e}")

            db.session.commit()
            print("✅ Data refreshed.")
        else:
            print("❌ API error.")

if __name__ == "__main__":
    fetch_and_store_countries()


