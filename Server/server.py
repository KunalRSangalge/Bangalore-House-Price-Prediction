from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
import os
import joblib

app = Flask(__name__, template_folder="../Client", static_folder="../Client")

# Load model & encoder
model = joblib.load("../Model/Pickle/model.pkl")
encoder = joblib.load("../Model/Pickle/encoder.pkl")
feature_columns = joblib.load("../Model/Pickle/feature_columns.pkl")

# ------------------- ROUTES -------------------

# Serve frontend
@app.route('/')
def home():
    return render_template("index.html")

# API: get all locations
@app.route('/locations', methods=['GET'])
def get_locations():
    locations = encoder.categories_[0].tolist()
    return jsonify(locations)

# API: predict price
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        location = data['location']
        sqft = float(data['total_sqft'])
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        # Build dataframe
        df = pd.DataFrame([[location, sqft, bhk, bath]], 
                          columns=['location','total_sqft','bhk','bath'])

        # One-hot encode location
        encoded_loc = encoder.transform(df[['location']])
        encoded_df = pd.DataFrame(encoded_loc,
                                  columns=encoder.get_feature_names_out(['location']))
        
        df = df.drop('location', axis=1)
        df_final = pd.concat([df, encoded_df], axis=1)

        # Align with training features
        df_final = df_final.reindex(columns=feature_columns, fill_value=0)

        # Predict
        pred = model.predict(df_final)[0]
        return jsonify({"predicted_price_lakhs": round(float(pred), 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ------------------- RUN -------------------
if __name__ == "__main__":
    app.run(debug=True)
