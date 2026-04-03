from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def create_vectorizer():
    return TfidfVectorizer(
        stop_words='english',
        max_features=7000,
        ngram_range=(1,2)  # BIG improvement
    )

def fit_transform(vectorizer, X_train):
    return vectorizer.fit_transform(X_train)

def transform(vectorizer, X_test):
    return vectorizer.transform(X_test)

def save_vectorizer(vectorizer):
    with open("models/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)