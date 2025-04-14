# 🌍 Country Data Dashboard

This app fetches data from the [REST Countries API](https://restcountries.com/), stores it in a database, and provides an interactive dashboard via Flask.

## ✨ Features
- Fetch & store real-time country data
- View countries with name, capital, population, region, and flag
- Live search and filter by region
- API endpoint `/countries` for programmatic access

## 🔧 Setup

```bash
git clone https://github.com/yourusername/country-data-dashboard.git
cd country-data-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py

