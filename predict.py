import joblib

# Load trained model and CountVectorizer
model = joblib.load("Models/sms_spam_classifier.pkl")
vectorizer = joblib.load("Models/count_vectorizer.pkl")

print("SMS Spam Classifier Ready!")
print("Type a message to check if it is Spam or Ham.")
print("Type 'exit' to stop.")

while True:
    text = input("\nEnter SMS: ")

    if text.lower() == "exit":
        print("Program stopped.")
        break

    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)[0]

    if prediction == 0:
        print("Prediction: SPAM 🚨")
    else:
        print("Prediction: HAM ✅")
