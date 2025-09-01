# 🏠 Bangalore House Price Prediction

This project predicts house prices in Bangalore based on **location, square footage, BHK, and number of bathrooms**.  
It includes **data preprocessing, EDA, feature engineering, model training, a Flask backend, and a simple frontend**.  

---

## 🚀 Features
- Cleaned and processed raw dataset from Kaggle.  
- Performed **Exploratory Data Analysis (EDA)** and **Feature Engineering**.  
- Trained multiple regression models:
  - Linear Regression
  - Lasso / Ridge Regression
  - Decision Tree
  - XGBoost (best performing model)  
- Best model achieved **R² score ~0.84**.  
- Built a **Flask API backend** with endpoints:
  - `/get_locations` → returns available location names.  
  - `/predict` → predicts house price given inputs.  
- Frontend built with **HTML, CSS, and JavaScript**:
  - Dropdown for locations (auto-fetched from backend).  
  - Buttons for selecting BHK & bathrooms.  
  - Displays predicted price in **Lakhs**.  
- Tested APIs using **Postman** before frontend integration.  

---

## 🛠️ Tech Stack
- **Python** (Flask, Pandas, NumPy, Scikit-learn, XGBoost)
- **Frontend**: HTML, CSS, JavaScript
- **Postman** for API testing
- **Pickle** for model serialization

---

## 📊 Model Performance
- Tried **Linear Regression, Lasso, Ridge, Decision Tree, XGBoost**
- Best model: **XGBoost with R² ≈ 0.84**
- Final model deployed for predictions

---


## 📂 Project Structure

```
HousePricePrediction/
│
├── Client/                     # Frontend (HTML, CSS, JS)
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── Server/                     # Flask backend
│   └── server.py
│
├── Model/                      # Saved ML models & notebooks
│   ├── Data_Cleaning.ipynb
│   ├── Feature_Engineering_and_Model_Training.ipynb
│   └── Pickle/
│       ├── model.pkl
│       └── encoder.pkl
│
├── Dataset/                    # Raw dataset
│   └── Bengaluru_House_Data.csv
│
├── .gitignore
└── requirements.txt
```
## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/HousePricePrediction.git
   cd HousePricePrediction
   ```

2. Create virtual environment & install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask server:
   ```bash
   cd Server
   python server.py
   ```

4. Open the frontend:
   - Navigate to `Client/index.html` in your browser
   - OR use `Live Server` in VS Code

---
## 🌟 Usage
- Enter **location, square footage, BHK, and bathrooms**
- Model predicts house price in **lakhs (INR)**

---

## 📌 Future Improvements
- Improve frontend UI/UX
- Deploy on **Heroku / Render / AWS**
- Add more features like amenities, year built, etc.

---

## 👨‍💻 Author
Kunal Rajesh Sangalge
