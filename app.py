from flask import Flask, render_template, request
from feature_engineering import FeatureEngineer
from custom_transformers import BooleanTransformer
import joblib
import pandas as pd

app = Flask(__name__)

# Load your trained model
artifacts = joblib.load('stroke_prediction_model.joblib')
model = artifacts['model']
preprocessor = artifacts['preprocessor']
best_threshold = artifacts['threshold']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_threshold = None
    if request.method == 'POST':
        try:
            # Get user input from the form
            age = float(request.form['age'])
            hypertension = int(request.form['hypertension'])
            heart_disease = int(request.form['heart_disease'])
            avg_glucose_level = float(request.form['avg_glucose_level'])
            bmi = float(request.form['bmi'])
            gender = request.form['gender']
            ever_married = request.form['ever_married']
            work_type = request.form['work_type']
            Residence_type = request.form['Residence_type']
            smoking_status = request.form['smoking_status']

            # Create a DataFrame from the input data
            input_data = pd.DataFrame({
                'age': [age],
                'hypertension': [hypertension],
                'heart_disease': [heart_disease],
                'avg_glucose_level': [avg_glucose_level],
                'bmi': [bmi],
                'gender': [gender],
                'ever_married': [ever_married],
                'work_type': [work_type],
                'Residence_type': [Residence_type],
                'smoking_status': [smoking_status]
            })

            processed_data = preprocessor.transform(input_data)
            prediction = model.predict_proba(processed_data)[:, 1][0]
            prediction_threshold = (prediction >= best_threshold).astype(int)

        except ValueError:
            prediction = "Invalid input. Please enter valid numerical values."

    return render_template('index.html', prediction_threshold=prediction_threshold)

if __name__ == '__main__':
    app.run(debug=True)