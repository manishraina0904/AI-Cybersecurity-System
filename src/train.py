from src.preprocess import load_data, preprocess_data, split_data
from src.feature import create_vectorizer, fit_transform, transform, save_vectorizer
from src.model import train_models, save_model

def train_pipeline():
    df = load_data("data/emails.csv")
    df = preprocess_data(df)

    X_train, X_test, y_train, y_test = split_data(df)

    vectorizer = create_vectorizer()
    X_train_tfidf = fit_transform(vectorizer, X_train)
    X_test_tfidf = transform(vectorizer, X_test)

    model = train_models(X_train_tfidf, y_train, X_test_tfidf, y_test)

    save_model(model)
    save_vectorizer(vectorizer)

    return X_test, y_test, vectorizer, model