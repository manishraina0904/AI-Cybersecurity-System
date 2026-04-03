from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

def train_models(X_train, y_train, X_test, y_test):
    models = {
        "Logistic": LogisticRegression(max_iter=1000, class_weight='balanced'),
        "NaiveBayes": MultinomialNB()
    }

    best_model = None
    best_score = 0

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        print(f"{name} Accuracy: {acc}")

        if acc > best_score:
            best_score = acc
            best_model = model

    print(f"\nBest Model Selected: {best_score}")
    return best_model
def save_model(model):
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)