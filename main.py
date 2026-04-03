from src.train import train_pipeline
from src.evaluate import evaluate_model
from src.predict import predict_text

# Train + Evaluate
X_test, y_test, vectorizer, model = train_pipeline()
evaluate_model(model, vectorizer, X_test, y_test)

print("\n--- TEST SYSTEM ---")

while True:
    text = input("Enter message (or 'exit'): ")
    if text.lower() == "exit":
        break

    result = predict_text(text, model, vectorizer)
    print("Result:", result)