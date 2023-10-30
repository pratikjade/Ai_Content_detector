import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier

# Load and preprocess the data
# Replace 'your_dataset.csv' with the actual file path
data = pd.read_csv('dataset.csv')
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['label']

# Train the model
classifier = ExtraTreesClassifier(n_estimators=50,random_state=2)
classifier.fit(X, y)

# Define the prediction function
def predict(text):
    text_vectorized = vectorizer.transform([text])
    prediction = classifier.predict(text_vectorized)[0]
    if prediction == 'AI':
        score = classifier.predict_proba(text_vectorized)[0][0]
    else:
        score = 1 - classifier.predict_proba(text_vectorized)[0][1]
    response = [
        {
            'label': prediction,
            'score': round(float(score), 4)
        }
    ]
    return response

# Streamlit app
st.title("AI detector")

# Text input for prediction
text = st.text_area("Enter some text")

# Perform prediction if text is provided
if st.button('analaize', type="primary"):
    st.button("Reset")
    result = predict(text)
    st.json(result)
