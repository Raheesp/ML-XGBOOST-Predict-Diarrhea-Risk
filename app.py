from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained pipeline (StandardScaler + RFE + XGBoost)
pipeline = joblib.load("capstone_project_1_mali.pkl")

# 10 selected features used in both HTML and model
selected_feature_names = [
    'OOccupier', 'OldFA', 'ageyear_2014', 'vaccine_card_available',
    'child_weighing_type_', 'Changed_water_source', 'Aquatabs_used',
    'ORT_recipe', 'mosquito_net_correct', 'ORT_ingr_correct'
]

@app.route("/")
def home():
    return render_template("index.html", prediction_label=None, confidence_score=None, error=None)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect and convert inputs
        input_data = {}
        for feature in selected_feature_names:
            value = request.form.get(feature)
            if value is None or value.strip() == "":
                raise ValueError(f"Missing value for '{feature}'")
            try:
                input_data[feature] = float(value)
            except ValueError:
                raise ValueError(f"Invalid input for '{feature}': must be a number")

        # Prepare input as array
        full_input = [input_data[feature] for feature in selected_feature_names]
        features = np.array(full_input).reshape(1, -1)

        # Predict using full pipeline
        prediction = pipeline.predict(features)[0]
        prediction_prob = pipeline.predict_proba(features)[0][1] * 100
        prediction_label = "High Risk" if prediction == 1 else "Low Risk"

        return render_template("index.html",
                               prediction_label=prediction_label,
                               confidence_score=round(prediction_prob, 2),
                               error=None)

    except Exception as e:
        return render_template("index.html",
                               prediction_label=None,
                               confidence_score=None,
                               error=str(e))

if __name__ == "__main__":
    app.run(debug=True)