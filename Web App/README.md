# 🌐 Fake News Detector Web Application

A Flask-based web application that classifies news articles as real or fake using a machine learning model.

## 📋 Overview

This web application provides a user-friendly interface for detecting fake news articles. Users can input news text, and the application will analyze it using a pre-trained machine learning model to determine its authenticity.

## 🚀 Features

- **Simple Interface**: Clean, intuitive design for easy text input
- **Real-time Analysis**: Instant classification of news articles
- **Confidence Scoring**: Shows prediction confidence percentage
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technical Stack

- **Backend**: Flask web framework
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: Scikit-learn, Joblib
- **Text Processing**: NLTK for natural language processing
- **Styling**: Custom CSS with Font Awesome icons

## 📁 Project Structure

```
fake_news_detector_web_app/
├── app.py                 # Flask application
├── important instructions.txt      # App instructions
├── fake_news_model.joblib      # Trained ML model
├── fake_news_vectorizer.joblib # Text vectorizer
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css         # Stylesheet
└── templates/
    └── index.html        # Main HTML template
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

**Option A: Install from requirements.txt (Recommended)**
```bash
pip install -r requirements.txt
```

**Option B: Install packages individually**
```bash
pip install flask
pip install scikit-learn
pip install joblib
pip install numpy
pip install nltk
```

### Step 2: Download NLTK Data
```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## 🎯 How to Use

1. **Enter News Text**: Paste or type the news article you want to analyze into the text area
2. **Analyze**: Click the "Analyze News" button
3. **View Results**: See the prediction (True/Fake) and confidence level
4. **Repeat**: Clear the text area to analyze another article

## 🐛 Troubleshooting

### Common Issues

1. **Model not loading error**:
   - Ensure `fake_news_model.joblib` and `fake_news_vectorizer.joblib` are in the main directory

2. **NLTK errors**:
   - Verify NLTK data is downloaded correctly:
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('wordnet')
   nltk.download('omw-1.4')
   ```

3. **Import errors**:
   - Check all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

## 🆘 Support

For issues and questions:

- Check that all files are in the correct locations
- Verify all Python packages are installed correctly  
- Ensure your system meets the prerequisites

---

## 📞 Contact the Developer
If you need assistance or want to connect with the developer:

* **LinkedIn**: https://www.linkedin.com/in/ali-muhammed-salah
* **Kaggle**: https://www.kaggle.com/alimuhammed10
* **GitHub**: https://github.com/ali-muhammed-salah

---

**Note**: This is a demonstration tool. Always verify information through multiple reliable sources.
