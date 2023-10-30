from flask import Flask, render_template, request, jsonify
import joblib

# Create a Flask app
app = Flask(__name__)

# Load the vectorization and model
vectorizer = joblib.load('vectorizer.pkl')
model = joblib.load('model.pkl')

# Define the route for the HTML GUI
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle text analysis
# @app.route('/analyze', methods=['POST'])
# def analyze_text():
#     user_text = request.form['text']
    
#     # Vectorize the user input
#     user_text_vectorized = vectorizer.transform([user_text])
    
#     # Make predictions
#     predictions = model.predict(user_text_vectorized)

#     # Return the result as JSON
#     return jsonify({"is_human": bool(predictions[0])})


@app.route('/analyze', methods=['POST'])
def analyze_text():
    user_text = request.form['text']
    
    # Vectorize the user input
    user_text_vectorized = vectorizer.transform([user_text])
    
    # Make predictions
    predictions = model.predict(user_text_vectorized)

    # Print the prediction for debugging
    print(f"Prediction: {predictions[0]}")

    # Return the result as JSON
    return jsonify({"Prediction": (predictions[0])})



if __name__ == '__main__':
    app.run(debug=True)

    
