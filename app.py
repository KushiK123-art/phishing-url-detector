from flask import Flask, render_template, request
import pickle

from feature_extraction import extract_features
from api_checker import check_url_virustotal

app = Flask(__name__)

# Load trained model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Get URL from form
    url = request.form['url']

    # Extract features
    features = [extract_features(url)]

    # ML Prediction
    prediction = model.predict(features)[0]

    # Probability
    probability = model.predict_proba(features)[0]
    confidence = round(max(probability) * 100, 2)

    # VirusTotal API Check
    api_result = check_url_virustotal(url)

    # Final Result
    if prediction == 1:
        result = '⚠️ Phishing Website Detected'
    else:
        result = '✅ Legitimate Website'

    # Send to frontend
    return render_template(
        'index.html',
        prediction_text=result,
        confidence=confidence,
        api_result=api_result,
        url=url
    )


if __name__ == '__main__':
    app.run(debug=True)