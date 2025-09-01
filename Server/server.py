from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from flask_cors import CORS  # to allow frontend to connect

app = Flask(__name__)
CORS(app)

# Load model & encoder
model = pickle.load(open("../Model/Pickle/xgb_model.pkl", "rb"))
encoder = pickle.load(open("../Model/Pickle/location_encoder.pkl", "rb"))
columns = pickle.load(open("../Model/Pickle/feature_columns.pkl", "rb"))  # feature columns

# --- API ROUTES ---

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        location = data["location"]
        sqft = float(data["total_sqft"])
        bhk = int(data["bhk"])
        bath = int(data["bath"])

        # Create DataFrame
        df = pd.DataFrame([[location, sqft, bhk, bath]],
                          columns=["location", "total_sqft", "bhk", "bath"])

        # Encode location
        encoded_loc = encoder.transform(df[["location"]])
        encoded_df = pd.DataFrame(encoded_loc.toarray(),
                                  columns=encoder.get_feature_names_out(["location"]))

        # Final dataframe
        df = pd.concat([df.drop("location", axis=1), encoded_df], axis=1)

        # Add missing columns
        for col in columns:
            if col not in df.columns:
                df[col] = 0

        df = df[columns]  # keep column order same

        prediction = model.predict(df)[0]
        return jsonify({"predicted_price_lakhs": round(float(prediction), 2)})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/locations", methods=["GET"])
def get_locations():
    try:
        locations = list(encoder.categories_[0])  # all unique locations
        return jsonify({"locations": locations})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
