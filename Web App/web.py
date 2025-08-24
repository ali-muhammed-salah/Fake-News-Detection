from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)

# Initialize text preprocessing tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """
    Your exact preprocessing function from the Jupyter Notebook
    """
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\\"\\n""', ' ', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    return " ".join(lemmatizer.lemmatize(w) for w in words if w not in stop_words)

# Load your pre-trained model and vectorizer using joblib
try:
    model = joblib.load('fake_news_model.joblib')
    vectorizer = joblib.load('fake_news_vectorizer.joblib')
    print("Model and vectorizer loaded successfully using joblib!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    vectorizer = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news_text']
        
        if not news_text.strip():
            return jsonify({'error': 'Please enter some text to analyze.'})
        
        if model is None or vectorizer is None:
            return jsonify({
                'prediction': 'Error',
                'confidence': 0,
                'news_text': news_text[:200] + '...' if len(news_text) > 200 else news_text,
                'message': 'Model not loaded. Please check if model files are available.'
            })
        
        try:
            # Preprocess the input text
            processed_text = preprocess_text(news_text)
            print(f"Processed text: {processed_text}")
            
            # Vectorize the preprocessed text
            features = vectorizer.transform([processed_text])
            print(f"Feature shape: {features.shape}")
            print(f"Non-zero features: {features.nnz}")
            
            # Check if we have any features at all
            if features.nnz == 0:
                return jsonify({
                    'prediction': 'Inconclusive',
                    'confidence': 0,
                    'news_text': news_text[:200] + '...' if len(news_text) > 200 else news_text,
                    'message': 'The text did not contain enough features for analysis.'
                })
            
            # Make prediction
            prediction = model.predict(features)
            print(f"Raw prediction: {prediction}")
            
            # Get confidence score
            if hasattr(model, 'predict_proba'):
                probability = model.predict_proba(features)
                confidence = np.max(probability)
                print(f"Class probabilities: {probability}")
                
                # Determine prediction based on highest probability
                if probability[0][1] > probability[0][0]:
                    prediction_label = "True"
                else:
                    prediction_label = "Fake"
            else:
                confidence = 0.8
                # Determine prediction based on raw prediction
                if prediction[0] == 1:
                    prediction_label = "True"
                else:
                    prediction_label = "Fake"
            
            return jsonify({
                'prediction': prediction_label,
                'confidence': float(confidence),
                'news_text': news_text[:200] + '...' if len(news_text) > 200 else news_text
            })
            
        except Exception as e:
            print(f"Error during prediction: {e}")
            return jsonify({
                'prediction': 'Error',
                'confidence': 0,
                'news_text': news_text[:200] + '...' if len(news_text) > 200 else news_text,
                'message': f'Prediction error: {str(e)}'
            })

if __name__ == '__main__':
    app.run(debug=True)