from src.train import train_pipeline
from src.predict import predict_text

def run_tests():
    print("🔄 Training model...")
    X_test, y_test, vectorizer, model = train_pipeline()

    print("\n🧪 Running Large Test Suite...\n")

    test_cases = [

        # ===== PHISHING (40+) =====
        ("Win money now click link", "Phishing"),
        ("Congratulations you won cash prize", "Phishing"),
        ("Claim your free reward now", "Phishing"),
        ("Urgent! account blocked click here", "Phishing"),
        ("Get loan instantly no documents", "Phishing"),
        ("You have been selected for prize", "Phishing"),
        ("Click link to verify account", "Phishing"),
        ("Update your bank details now", "Phishing"),
        ("Free recharge offer click now", "Phishing"),
        ("Earn money from home easily", "Phishing"),
        ("Limited time offer act now", "Phishing"),
        ("Your account is suspended login now", "Phishing"),
        ("Winner! claim your gift now", "Phishing"),
        ("Exclusive deal just for you click", "Phishing"),
        ("You are selected for free gift", "Phishing"),
        ("Verify your identity immediately", "Phishing"),
        ("Claim lottery prize now", "Phishing"),
        ("Click here for cashback reward", "Phishing"),
        ("Update payment info urgently", "Phishing"),
        ("You won iphone click here", "Phishing"),
        ("Free netflix subscription claim now", "Phishing"),
        ("Reset your password now urgent", "Phishing"),
        ("Get free amazon voucher now", "Phishing"),
        ("Your bank account needs verification", "Phishing"),
        ("Click link to avoid account suspension", "Phishing"),
        ("Get rich quick scheme click now", "Phishing"),
        ("Instant approval loan apply now", "Phishing"),
        ("You have unclaimed reward click here", "Phishing"),
        ("Security alert login now", "Phishing"),
        ("Claim bonus before it expires", "Phishing"),
        ("Act fast limited offer", "Phishing"),
        ("Free gift card waiting click now", "Phishing"),
        ("Your package delivery pending click", "Phishing"),
        ("Unlock premium account now", "Phishing"),
        ("Win big cash today click here", "Phishing"),
        ("Verify KYC immediately click", "Phishing"),
        ("Suspicious login detected click now", "Phishing"),
        ("Claim refund immediately click link", "Phishing"),
        ("Your sim will be blocked update now", "Phishing"),
        ("Urgent payment required click here", "Phishing"),

        # ===== LEGITIMATE (40+) =====
        ("Hey are you coming today", "Legitimate"),
        ("Let's meet tomorrow", "Legitimate"),
        ("Call me when you reach", "Legitimate"),
        ("Send me notes please", "Legitimate"),
        ("I will join meeting at 5pm", "Legitimate"),
        ("Where are you right now", "Legitimate"),
        ("Did you finish the assignment", "Legitimate"),
        ("Let’s go for dinner tonight", "Legitimate"),
        ("Can you help me with this", "Legitimate"),
        ("I will call you later", "Legitimate"),
        ("Please send the file", "Legitimate"),
        ("Meeting is scheduled at 10am", "Legitimate"),
        ("Happy birthday bro", "Legitimate"),
        ("See you soon", "Legitimate"),
        ("Let me know your plan", "Legitimate"),
        ("Are you available now", "Legitimate"),
        ("Please check your email", "Legitimate"),
        ("I reached home safely", "Legitimate"),
        ("Let’s discuss project tomorrow", "Legitimate"),
        ("Thanks for your help", "Legitimate"),
        ("Where should we meet", "Legitimate"),
        ("I am running late", "Legitimate"),
        ("Can you pick me up", "Legitimate"),
        ("Good morning have a nice day", "Legitimate"),
        ("I will send details soon", "Legitimate"),
        ("Call me when free", "Legitimate"),
        ("Let's play cricket today", "Legitimate"),
        ("Do you have class today", "Legitimate"),
        ("I will text you later", "Legitimate"),
        ("Please confirm attendance", "Legitimate"),
        ("What is your location", "Legitimate"),
        ("I am in the office", "Legitimate"),
        ("Can we reschedule meeting", "Legitimate"),
        ("Let me know when you arrive", "Legitimate"),
        ("Have you eaten lunch", "Legitimate"),
        ("I will reach in 10 minutes", "Legitimate"),
        ("Let's watch a movie", "Legitimate"),
        ("Are you at home", "Legitimate"),
        ("Please bring the documents", "Legitimate"),
        ("See you at the event", "Legitimate"),
    ]

    correct = 0

    for text, expected in test_cases:
        result = predict_text(text, model, vectorizer)
        predicted = "Phishing" if "Phishing" in result else "Legitimate"

        print(f"Input: {text}")
        print(f"Expected: {expected} | Predicted: {predicted}\n")

        if predicted == expected:
            correct += 1

    accuracy = correct / len(test_cases)

    print("===================================")
    print(f"Final Test Accuracy: {accuracy:.2f}")
    print("===================================")


if __name__ == "__main__":
    run_tests()