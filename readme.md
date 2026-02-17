# SMS Spam Classifier

## Project Overview
This project classifies SMS messages as "ham" (not spam) or "spam" using Machine Learning.

## Dataset
- UCI SMS Spam Collection (5572 messages)
- Stored in data/ folder

## Model
- Logistic Regression with CountVectorizer features
- Oversampling to balance spam messages

## Results
- Accuracy: 0.98
- Spam F1-score: 0.93

## How to Use
1. Install dependencies:
   pip install -r requirements.txt
2. Load model:
   import joblib
   model = joblib.load("models/sms_spam_classifier.pkl")
   cv = joblib.load("models/count_vectorizer.pkl")
3. Predict:
   message = ["Free entry, win a prize!"]
   message_vec = cv.transform(message)
   prediction = model.predict(message_vec)
   print(prediction)
