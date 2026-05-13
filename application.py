import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

application = Flask(__name__)
app = application

# Load model and scaler file
try:
    ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
    standard_scaler = pickle.load(open("models/scaler.pkl", "rb"))
    print("Load successfully")
except Exception as e:
    print("Error:", e)


# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Prediction Page
@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    # fetch form data
    if request.method == "POST":
        # Convert data into float
        input_data = [
            float(request.form.get("study_hours", 0)),
            float(request.form.get("prev_score", 0)),
            float(request.form.get("sleep_hour", 0)),
            float(request.form.get("sample_ques", 0)),
            float(request.form.get("extra_curr_Yes", 0)),
        ]
        # handle negavtive values 
        input_data = [max(0, val) for val in input_data]

        # Feature names
        features = [
            "Hours Studied",
            "Previous Scores",
            "Sleep Hours",
            "Sample Question Papers Practiced",
            "Extracurricular Activities_Yes",
        ]
        # Make dataframe for model
        df_input = pd.DataFrame([input_data], columns=features)
        new_scaled_data = standard_scaler.transform(df_input)
        result = ridge_model.predict(new_scaled_data)
        return render_template("home.html", results=round(result[0], 2))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
