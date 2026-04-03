from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from src.feature import transform

def evaluate_model(model, vectorizer, X_test, y_test):
    X_test_tfidf = transform(vectorizer, X_test)
    y_pred = model.predict(X_test_tfidf)

    print("\nFinal Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))