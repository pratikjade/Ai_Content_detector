import joblib

# Load the vectorization model
vectorizer = joblib.load('vectorizer.pkl')

# Load the machine learning model
model = joblib.load('model.pkl')

# New text data
user_text = input("Enter a text for prediction: ")

# Vectorize the new data
vect_input=vectorizer.transform([user_text])

# Make predictions
predictions = model.predict(vect_input)

# Print the predictions
print("Predicted:", predictions[0])