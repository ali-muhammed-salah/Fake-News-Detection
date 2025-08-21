# 📰 Fake News Detection – NLP Task

### 🚀 **ELEVVO Internship Project**

* 👤 **Author:** Ali Muhammed  
* 🧠 **Task Level:** 2  
* 🚀 **Task Number:** 3

---

## 🎯 **Objective**
Build a machine learning model to classify news articles as **Real** ✅ or **Fake** ❌ using Natural Language Processing (NLP) techniques.

---

## 📁 **Dataset**

* **Files:** `train.csv`, `test.csv`  
* **Columns Used:**
  * `title`  (Text)  
  * `text`  (Text)
  * `subject`  (Text)
  * `date`  (datetime)
  * `label` (Binary target: `fake` / `real`)
* **Rows Used:** All **\~44,898 reviews** from the dataset

---

## 🛠 **Tools & Libraries**
* 🐍 Python  
* 📊 Pandas  
* 🔡 re (Regular Expressions)  
* ✂️ NLTK  
* 🔢 Collections  
* 📈 Matplotlib  
* ☁️ WordCloud  
* 🤖 Scikit-learn  

---

## 🔄 **Workflow Overview**

### 🧹 **1. Data Cleaning & Preprocessing**
* 🔡 Converted text to lowercase  
* 🚫 Removed stopwords and applied lemmatization  
* ✂️ Tokenized text where needed for analysis

---

### ✨ **2. Feature Extraction**
* 🧮 Used **TF-IDF Vectorizer** to convert text into numerical features for the model.

---

### 🧠 **3. Model Building**
* 🔍 Used Logistic Regression Model and Multinomial Naive Bayes Model (Bonus) as the classification algorithms
* 🗂️ Split dataset into 80% training and 20% testing

---

### 📊 **4. Model Evaluation**
* 📑 Used metrics like **Accuracy**, **Confusion Matrix**, **Classification Report** and **F1 Score**

---

## 🎨 **Visualizations**
* ☁️ Generated WordCloud showing the **most frequent words** in news articles.

---

## 📊 **Model Insights**

| **💡 Model**         | **🧩 Type**          | **🎯 Accuracy** |
| ----------------- | ----------------- | ------------ |
| 📈 Logistic Regression        | Classical ML      | ~99% ✅         |

---

## 💡 **Key Learnings**

* Multi-class classification using classical methods
* Text preprocessing and feature engineering  
* Evaluating and visualizing NLP models  

---

> **Note:** This task focused on classic NLP (no deep learning) to strengthen fundamental understanding before moving to advanced transformer models.

