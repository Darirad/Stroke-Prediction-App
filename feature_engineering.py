from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        self.glucose_mean_ = X["avg_glucose_level"].mean()
        return self

    def transform(self, X):
        X = X.copy()

        X["bmi_x_age"] = X["bmi"] * X["age"] ** 2
        #X["high_risk_group"] = (
        #    (X["ever_married"] == "No")
        #    & ((X["smoking_status"] == "smoked"))
        #    | (X["smoking_status"] == "formerly smoked")
        #).astype(int)
        X["Married_Young"] = (X["ever_married"] == "Yes") * (
            X["age"] < 50
        )
        #X["Smoker_SelfEmployed"] = (
        #    (X["smoking_status"] == "smokes")
        #    & (X["work_type"] == "Self-employed")
        #).astype(int)
        #X["age_smoking_interaction"] = X["age"] * (
        #    X["smoking_status"] == "smokes"
        #).astype(int)
        X["hypertension_heart_disease"] = (
            X["hypertension"] * X["heart_disease"]
        )
        #X["potentially_isolated"] = (
        #    (X["ever_married"] == "No")
        #    & (X["work_type"] == "Never_worked")
        #).astype(int)
        X["old_single"] = (
            (X["ever_married"] == "No") & (X["age"] > 50)
        ).astype(int)
        return X
