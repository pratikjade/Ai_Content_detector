import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import ExtraTreesClassifier

# Load and preprocess the data
data = pd.read_csv('dataset.csv')
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['label']

# Train the model
classifier = ExtraTreesClassifier(n_estimators=50, random_state=2)
classifier.fit(X, y)

# Define the prediction function
def predict(text):
    if not text:
        return [{'label': 'Error', 'score': 0}]
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
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1698945746290-a9d1cc575e77?auto=format&fit=crop&q=80&w=1946&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}
[data-testid="stHeader"] {
    background-color: transparent;
}

data-testid="stToolbar"{
right: 2rem;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Initialize session state
if 'started' not in st.session_state:
    st.session_state.started = False

# Check if the "Get Started" button is clicked
if not st.session_state.started:
    st.session_state.started = False

# Check if the "Get Started" button is clicked
if not st.session_state.started:
    st.markdown("<h1 style='display: flex; text-align:center;justify-content: center; align-items: center; font-size: 50px ; height: 55vh;'>Welcome to AI Content Detector</h1>", unsafe_allow_html=True)
    st.markdown("")
    columns = st.columns((2, 1, 2))

    # Use custom CSS to style the button

    button_pressed = """
        <style>
            div.stButton > button:first-child {
            background-color: #000;
            border: 1px solid #000;
            border-radius: 20px;
            color: #fff;
            cursor: pointer;
            display: inline-block;
            font-family: ITCAvantGardeStd-Bk, Arial, sans-serif;
            font-size: 20px;
            font-weight: 50;
            line-height: 40px;
            padding: 12px 40px;
            text-align: center;
            text-transform: none;
            user-select: none;
            -webkit-user-select: none;
            width: max-content;
            }
            div.stButton > button:first-child:hover {
                background-color: #ffffff;
                border: 1px solid #000;
                color: #000000;
                font-family: monospace;
            }
        </style>
    """
    st.markdown(button_pressed, unsafe_allow_html=True)

    button_pressed = columns[1].button("Get Started", key="get_started_button", on_click=lambda: st.session_state.__setitem__('started', True))
    if button_pressed:
        st.session_state.started = True
        st.markdown(
        """
        <script>
            var button = document.querySelector('.stButton button.button-50');
            button.style.backgroundColor = "#000"; // Change background color to black
        </script>
        """,
        unsafe_allow_html=True,
    )

# If the app has been started
if st.session_state.started:
    st.markdown("")

    # Use HTML to create a heading in the main app
    st.markdown("<h1 style='text-align:center;font-size: 50px;height: 15vh;'>Detect AI Content</h1>", unsafe_allow_html=True)

    # Add some space
    st.markdown("<br>", unsafe_allow_html=True)

    # Create a text input with a label
    text = st.text_area(" ", placeholder="Type your text here", height=200)

    # Add space between input and button
    st.markdown("<br>", unsafe_allow_html=True)

    # Use CSS to style the button
    button_style = """
        <style>
            div.stButton > button:first-child {
                background-color: #000;
                color: #fff;
                width: 150px;
                Height: 50px;
                display: flex;
                float: right;
                color: white;
                font-size: 18px;
                border: none;
                cursor: pointer;
                margin-right: 16cm;
            }
            div.stButton > button:first-child:hover {
                background-color: #fff;
                color: #000000;
                border: 1px solid #000;
            }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # Create a button to trigger the analysis
    if st.button("Detect Text"):
        result = predict(text)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h2>Result:</h2>", unsafe_allow_html=True)

        if result[0]['label'] == 'Error':
            label_color = "color: #FF2400;"
            progress_color = "#FF2400"
        elif result[0]['label'] == 'AI':
            label_color = "color: #FF2400;"
            progress_color = "#FF2400"
        else:
            label_color = "color: #00B140;"
            progress_color = "#00B140"

        # Use HTML to style the prediction result
        if result[0]['label'] == 'Error':
            result_html = f"<p style='font-size: 30px; font-weight: bold; {label_color}'>Error: Please enter text..💀</p>"
        elif result[0]['label'] == 'AI':
            result_html = f"<p style='font-size: 30px; font-weight: bold; {label_color}'>Predicted Label: {result[0]['label']} 😢</p>"
        else:
            result_html = f"<p style='font-size: 30px; font-weight: bold; {label_color}'>Predicted Label: {result[0]['label']} 🎉</p>"
        st.markdown(result_html, unsafe_allow_html=True)

        if result[0]['label'] != 'Error':

            # Add a status bar for the Confidence Score with percentages
            confidence_percentage = result[0]['score'] * 100
            
            score_html = f"<p style='font-size: 25px;{label_color}'>This text is likely to be written by {result[0]['label']} is {confidence_percentage}%</p>"
            st.markdown(score_html, unsafe_allow_html=True)
            progress_bar_css = f"""
            <style>
                .stProgress > div > div > div > div {{
                    background-color: {progress_color};
                }}
            </style>
            """
            st.markdown(progress_bar_css, unsafe_allow_html=True)
            st.progress(result[0]['score'])




st.markdown(
        """
        <div style="position: absolute; bottom: -5.8cm;">
            <b color: #000000;">Site is not optimize for mobile view.</b>
        </div>
        """,
        unsafe_allow_html=True
    )



