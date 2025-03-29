🌍 Country Data Aggregator and Insights Dashboard
This project fetches country data using the REST Countries API, stores it in a database, and provides an insights dashboard.

🛠 Features
✅ Fetches real-time country data using REST API
✅ Stores data in an SQLite database using Flask-SQLAlchemy
✅ Provides an API endpoint to retrieve stored country data
✅ Basic frontend dashboard to display country insights

📥 Installation Guide
Follow these steps to set up and run the project.

1️⃣ Clone the Repository
Open a terminal (Command Prompt/PowerShell for Windows, Terminal for macOS/Linux) and run:

bash
Copy
Edit
git clone https://github.com/Bhagyashree-kaji/country_data_dashboard.git
Navigate into the project folder:

bash
Copy
Edit
cd country_data_dashboard
2️⃣ Set Up a Virtual Environment
For Windows:
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
For macOS/Linux:
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
Run:

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Flask Application
bash
Copy
Edit
python app.py
After running the command, you should see output like this:

nginx
Copy
Edit
Running on http://127.0.0.1:5000/
Open a browser and go to http://127.0.0.1:5000/countries to verify API responses.

📂 Project Structure
csharp
Copy
Edit
country_data_dashboard/
│── static/ # CSS, JavaScript, Images
│── templates/ # HTML Templates
│── venv/ # Virtual Environment
│── app.py # Main Flask App
│── models.py # Database Models
│── requirements.txt # Dependencies
│── config.py # Configuration File
│── README.md # Project Documentation
🛠 API Usage
Fetch All Countries
Endpoint: /countries

Method: GET

Response:

json
Copy
Edit
[
{
"name": "India",
"population": 1400000000,
"region": "Asia"
},
{
"name": "United States",
"population": 331000000,
"region": "Americas"
}
]
🚀 Next Steps
🔹 Improve UI with a dashboard
🔹 Add search and filter features
🔹 Deploy the project
