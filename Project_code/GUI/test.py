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

# Create a Streamlit app
st.set_page_config(
    page_title="AI Detector",
    page_icon="🤖",
    layout="wide",
)

# Initialize session state
if 'started' not in st.session_state:
    st.session_state.started = False

# Check if the "Get Started" button is clicked
if not st.session_state.started:
    st.markdown("<div style='display: flex; justify-content: center; align-items: center; height: 80vh;'><h1>Welcome to AI Detector</h1></div>", unsafe_allow_html=True)
    if st.button("Get Started"):
        st.session_state.started = True

# If the app has been started
if st.session_state.started:
    st.title("AI Detector")
    
    # Use HTML to create a heading in the main app
    st.markdown("<h1 style='text-align:center;'>Detect AI Content</h1>", unsafe_allow_html=True)

    # Add some space
    st.markdown("<br>", unsafe_allow_html=True)

    # Create a text input with a label
    text = st.text_area("Enter some text", height=100)

    # Add space between input and button
    st.markdown("<br>", unsafe_allow_html=True)

    # Use CSS to style the button
    button_style = """
        <style>
            div.stButton > button:first-child {
                background-color: #4CAF50;
                color: white;
                font-size: 18px;
                border: none;
                cursor: pointer;
            }
            div.stButton > button:first-child:hover {
                background-color: #45a049;
            }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # Create a button to trigger the analysis
    if st.button("Analyze"):
        result = predict(text)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h2>Analysis Result:</h2>", unsafe_allow_html=True)

        if result[0]['label'] == 'AI':
            label_color = "color: #4CAF50;"
        else:
            label_color = "color: #FF5733;"

        # Use HTML to style the prediction result
        result_html = f"<p style='font-size: 20px; font-weight: bold; {label_color}'>Predicted Label: {result[0]['label']}</p>"
        score_html = f"<p style='font-size: 16px;'>Confidence Score: {result[0]['score']:.2%}</p>"
        st.markdown(result_html, unsafe_allow_html=True)

        # Add a status bar for the Confidence Score with percentages
            # Add a status bar for the Confidence Score with percentages
        score_html = f"<p style='font-size: 16px;'>Probability this text was entirely written by {result[0]['label']},is  {result[0]['score']}</p>"
        st.markdown(score_html, unsafe_allow_html=True)
        st.progress(result[0]['score'])