from flask import Flask, render_template, request
from utils.scraper import fetch_flight_data
from utils.analyzer import analyze_flight_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    insights = []
    chart_data = {}

    if request.method == "POST":
        origin = request.form.get("origin").upper()
        destination = request.form.get("destination").upper()

        # Step 1: Fetch data
        flight_data = fetch_flight_data(origin, destination)

        # Step 2: Analyze data
        insights, chart_data = analyze_flight_data(origin, destination, flight_data)

    return render_template("index.html", insights=insights, chart_data=chart_data)

if __name__ == "__main__":
    app.run(debug=True)
