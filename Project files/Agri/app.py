# ============================================================
# OptiCrop - Flask Backend
# Epic 5 : Build Python Backend
# ============================================================

import pickle
import pandas as pd
from flask import Flask, render_template, request

# ------------------------------------------------------------
# Create Flask App
# ------------------------------------------------------------

app = Flask(__name__)

# ------------------------------------------------------------
# Load Trained Model
# ------------------------------------------------------------

model = pickle.load(open("model.pkl", "rb"))

# ------------------------------------------------------------
# Home Page
# ------------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")

# ------------------------------------------------------------
# About Page
# ------------------------------------------------------------

@app.route("/about")
def about():
    return render_template("about.html")

# ------------------------------------------------------------
# Find Your Crop Page
# ------------------------------------------------------------

@app.route("/findyourcrop")
def findyourcrop():
    return render_template("findyourcrop.html")

# ------------------------------------------------------------
# Prediction
# ------------------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        input_data = pd.DataFrame(
            [[N, P, K, temperature, humidity, ph, rainfall]],
            columns=[
                "N",
                "P",
                "K",
                "temperature",
                "humidity",
                "ph",
                "rainfall"
            ]
        )

        prediction = model.predict(input_data)

        return render_template(
            "findyourcrop.html",
            prediction_text=f"Best Crop for Given Conditions: {prediction[0]}"
        )

    except Exception as e:

        return render_template(
            "findyourcrop.html",
            prediction_text=f"Error : {e}"
        )
# ------------------------------------------------------------
# Run Application
# ------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)