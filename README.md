# 🧠 Stroke Prediction App

This project predicts the likelihood of a person experiencing a **stroke**, using patient health and demographic data. It includes:

- ✨ Feature engineering to enhance model performance
- 📊 Exploratory Data Analysis (EDA)
- 🤖 A powerful XGBoost and Random Forest models trained with **SMOTE** to handle class imbalance
- 🖥️ A web interface built with Flask using XGBoost model
- 📦 A Dockerized deployment setup

---

## 📁 Project Structure

```bash
├── Initial_EDA.ipynb              # Exploratory Data Analysis notebook
├── Stroke_Prediction.ipynb        # Feature engineering, modeling, evaluation
├── feature_engineering.py         # Custom FeatureEngineering class
├── stroke_prediction_model.joblib # Trained XGBoost model
├── app.py                         # Flask web app
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker image definition
├── .dockerignore                  # Files ignored in Docker context
├── templates/
│   └── index.html                 # HTML template for the app
```


---

## 🔍 Summary of Modeling Results

- **Model**: XGBoost Classifier  

- **Resampling**: SMOTE (Synthetic Minority Over-sampling Technique)  
- **Custom threshold (optimized on validation set)**: `0.06`  

### 🧪 Validation Metrics

| Metric                    | Score     |
|---------------------------|-----------|
| Balanced Accuracy         | 0.739     |
| ROC AUC                   | 0.770     |
| f1 score                  | 0.861     |
| Class 1 Recall            | 0.800     |
| Class 1 Precision         | 0.113     |

### 🧾 Test Metrics

| Metric                    | Score     |
|---------------------------|-----------|
| Balanced Accuracy         | 0.735     |
| ROC AUC                   | 0.734     |
| Class 1 Recall            | 0.780     |
| Class 1 Precision         | 0.114     |

✅ **Confusion Matrix (Test)**:

[[670 302] 
[ 11 39]]



- **Model**: Random Forest Classifier  

- **Resampling**: SMOTE (Synthetic Minority Over-sampling Technique)  
- **Custom threshold (optimized on validation set)**: `0.13`  

### 🧪 Validation Metrics

| Metric                    | Score     |
|---------------------------|-----------|
| Balanced Accuracy         | 0.779     |
| ROC AUC                   | 0.791     |
| f1 score                  | 0.690     |
| Class 1 Recall            | 1.0       |
| Class 1 Precision         | 0.104     |

### 🧾 Test Metrics

| Metric                    | Score     |
|---------------------------|-----------|
| Balanced Accuracy         | 0.713     |
| ROC AUC                   | 0.790     |
| Class 1 Recall            | 0.860     |
| Class 1 Precision         | 0.092     |

✅ **Confusion Matrix (Test)**:

[[550 422] 
[ 7 43]]


---

## 💡 Key Feature Engineering Insights

The following engineered features had a **strong positive effect** on the model’s performance:

| Feature                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `bmi_x_age`                | Product of BMI and Age                                                      |
| `Married_Young`            | Boolean: `age < 50` and `ever_married = Yes`                                |
| `age_smoking_interaction` | Interaction term: age × smoker status                                       |
| `old_single`               | Boolean: `age > 50` and `ever_married = No`                                 |

These features significantly improved recall for class 1 (stroke cases) from ~30% to **over 70%**.

---



## 🛠️ Setup

1.Clone this repository:

```bash
git clone https://github.com/Darirad/Stroke-Prediction-App.git 
cd Stroke-Prediction-App
```


2. Install Dependencies

```bash
pip install -r requirements.txt
```

2. Run the Flask App (Development)

```bash
python app.py
```
Then open your browser and go to:
http://127.0.0.1:5000


## 🚢 Running the App with Docker

Make sure you have **Docker installed**, then in the project root:

### Build the Image

```bash
docker build -t stroke-prediction-app .
```

### Run the Container

```bash
docker run -d -p 5000:5000 --name stroke-app stroke-prediction-app
```
- Access at: http://localhost:5000
- Stop the container:

    ```bash
    docker stop stroke-app && docker rm stroke-app
    ```

View Logs
```bash
docker logs -f stroke-app
```
## 🏁 Conclusion

Our analysis compared two optimized models for stroke risk prediction, both addressing severe class imbalance through SMOTE and custom threshold tuning:

### Model Performance Summary
| Model          | Threshold | Balanced Accuracy | ROC AUC | Recall (Stroke) | Precision (Stroke) |
|----------------|-----------|-------------------|---------|-----------------|--------------------|
| **Random Forest** | 0.13      | 0.713             | 0.791   | 86.0%           | 0.092              |
| **XGBoost** | 0.06    | 0.735             | 0.734   | 78.0%           | 0.112              |

### Key Findings
- **Feature Engineering Impact**:
  - Created features (`bmi_x_age`, `Married_Young`, etc.) improved minority class recall by **>140%** (from ~30% baseline)
  - Demonstrated the value of domain-specific feature creation

- **Clinical Trade-offs**:
  - **Random Forest** is superior for *screening* (86% recall catches most strokes)
  - **XGBoost** provides better *balance* (73.4% recall/specificity)
  - Both models show the expected precision-recall tension in medical AI

## 🚀 Future Improvements

To further enhance the model's performance and clinical utility, the following areas should be explored:

1.  **Improve Precision for Class 1:**
    * **Further Feature Engineering:** Investigate and engineer additional features that could help the model better discriminate between true positive and false positive stroke predictions. This could involve exploring more complex interactions between existing features or incorporating external data sources (if available and ethical).
    * **Advanced Modeling Techniques:** Experiment with other classification algorithms that might offer a better balance between recall and precision for imbalanced datasets, such as LightGBM, CatBoost, or ensemble methods.
    * **Cost-Sensitive Learning:** Implement cost-sensitive learning techniques where misclassifying a stroke case (false negative) is penalized more heavily than a false positive, aligning the model's objective with the clinical priorities.

2.  **External Data Integration:**
    * **Medical History:** If available and with appropriate ethical considerations, incorporating more detailed medical history (e.g., prior transient ischemic attacks (TIAs), cholesterol levels, blood pressure history) could significantly improve predictive power.
    * **Lifestyle Factors:** Including more granular lifestyle information (e.g., diet, exercise habits) might reveal further predictive patterns.

3.  **Deployment and Monitoring:**
    * **Implement continuous monitoring:** Establish a system to track the model's performance in a live environment, detect potential drift in data or performance, and trigger retraining when necessary.

By focusing on these future improvements, we can strive to create a more accurate, reliable, and clinically valuable stroke risk prediction tool.