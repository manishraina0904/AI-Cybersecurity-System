import pickle
from src.feature import transform
from src.preprocess import clean_text

def load_model():
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("models/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

def predict_text(text, model, vectorizer):
    from src.preprocess import clean_text

    text = clean_text(text)
    text_tfidf = vectorizer.transform([text])

    prob = model.predict_proba(text_tfidf)[0][1]

    # 🔥 Rule-based boost (VERY IMPORTANT)
    suspicious_keywords = [
        "win", "free", "click", "offer", "urgent",
        "prize", "reward", "claim", "loan", "cash",
        "verify", "account", "bank", "password"
    ]

    keyword_flag = any(word in text for word in suspicious_keywords)

    # 🔥 Hybrid decision
    if prob > 0.25 or keyword_flag:
        return f"Phishing (confidence: {prob:.2f})"
    else:
        return f"Legitimate (confidence: {prob:.2f})"