from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import FunctionTransformer

def boolean_to_int(x):
    return x.astype(int)

class BooleanTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.transformer = FunctionTransformer(boolean_to_int)

    def fit(self, X, y=None):
        self.transformer.fit(X, y)
        return self

    def transform(self, X):
        return self.transformer.transform(X)

    def get_feature_names_out(self, input_features=None):
        return input_features
