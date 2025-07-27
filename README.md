# 🧪 Diarrhea Risk Prediction Web App

This project is a **Flask-based web application** that uses a trained machine learning model to predict the **risk of diarrhea in children** based on household and healthcare-related information. The data used is from a real-world health study conducted in **Urban Mali, 2014**.

## 📊 Project Overview

The application allows users to input various child and household health details and get a **prediction of diarrhea risk (High/Low)** along with a **confidence score**. The model was trained using **XGBoost** and **RFE (Recursive Feature Elimination)** to select the most relevant features.

<img width="1892" height="962" alt="Image" src="https://github.com/user-attachments/assets/f5cc8d20-7161-4a35-8930-85a133b002e2" />
<img width="1898" height="952" alt="Image" src="https://github.com/user-attachments/assets/a68902cc-5329-4ecb-b55e-af8b0c6e03f5" />

---

## 🚀 Features

- 🧠 Machine learning model with feature selection (RFE)
- 🎯 Risk prediction (High Risk / Low Risk)
- 📈 Visual confidence score using a dynamic progress bar
- 📄 Form inputs with descriptions for easy understanding
- 💡 Animated transitions using CSS
- 💻 Fully responsive Bootstrap UI

---

## 📁 Folder Structure

```
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Main frontend HTML file
├── static/
│   └── background/
│       └── image.jpg       # Background image for the UI
├── capstone_project_1_mali.pkl  # Trained ML pipeline (scaler + RFE + XGB)
└── README.md               # Project overview and documentation
```

---

## 🧠 Selected Features Used in Model

The ML model uses the following 10 features:

| Feature Name              | Description |
|--------------------------|-------------|
| `OOccupier`              | If the person is the main house owner (1 = Yes, 0 = No) |
| `OldFA`                  | Number of old health program visits (numeric) |
| `ageyear_2014`           | Age of the child in years as of 2014 |
| `vaccine_card_available` | Whether a vaccine card was shown (1 = Yes, 0 = No) |
| `child_weighing_type_`   | Whether the child was weighed in a clinic (1 = Yes, 0 = No) |
| `Changed_water_source`   | Whether the water source was changed recently (1 = Yes, 0 = No) |
| `Aquatabs_used`          | Use of Aquatabs (water cleaning tablets) (1 = Yes, 0 = No) |
| `ORT_recipe`             | Knowledge of ORT recipe (1 = Yes, 0 = No) |
| `mosquito_net_correct`   | Proper use of mosquito net (1 = Yes, 0 = No) |
| `ORT_ingr_correct`       | Knowledge of correct ORT ingredients (1 = Yes, 0 = No) |

---

## ⚙️ How to Run the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/diarrhea-risk-predictor.git
   cd diarrhea-risk-predictor
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   python app.py
   ```

4. Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Example Test Case

| Feature                   | Value |
|---------------------------|-------|
| Occupier Type             | 1     |
| OldFA                     | 2     |
| Age (2014)                | 3.5   |
| Vaccine Card Available    | 1     |
| Child Weighing Type       | 1     |
| Changed Water Source      | 0     |
| Aquatabs Used             | 1     |
| ORT Recipe Known          | 1     |
| Mosquito Net Correct      | 1     |
| ORT Ingredients Known     | 1     |

**Expected Output:**
```
Prediction: Low Risk
Confidence Score: 9.82%
```

---

## 📚 Dataset Info

The dataset used is derived from:
> **"The Effects of Community Health Worker Visits and Primary Care Subsidies on Health Behavior and Health Outcomes for Children in Urban Mali (2014)"**

---

## 🤝 Acknowledgements

- [World Bank Microdata Library](https://microdata.worldbank.org/)
- [XGBoost](https://xgboost.readthedocs.io/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)

---

## 🛠️ Future Enhancements

- Add downloadable prediction report (PDF)
- Enable real-time charts using Chart.js or D3.js
- Deploy the app on Heroku or Render

---

## 🧑‍💻 Author

**Mohammed Rahees P**  
Final Year B.Tech – AI & Data Science  
📬 [LinkedIn](https://www.linkedin.com) 

