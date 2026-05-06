# 🩺 Medical AI Chatbot with Explainable AI (XAI)

## 📌 Project Overview

This project is a **Medical AI Chatbot** that predicts possible diseases based on user-provided symptoms.
It uses **Machine Learning (Random Forest)** and provides:

* Disease prediction
* Confidence score
* Explanation of predictions (Explainable AI)

The system includes:

* Smart symptom suggestions (dropdown)
* Natural language input (NLP)
* Interactive chat interface

---

## 🎯 Objectives

* Develop a disease prediction system using machine learning
* Improve usability through a chatbot interface
* Provide explainable AI outputs
* Demonstrate real-world application of AI

---

## 🧠 Technologies Used

### Programming Language

* Python 3.10+ (Recommended: Python 3.10 or 3.11)

### Backend

* Flask (v2.3+)
* Flask-CORS (v4.0+)

### Data Processing & ML

* Pandas (v2.0+)
* NumPy (v1.24+)
* Scikit-learn (v1.3+)
* Joblib (v1.3+)

### Frontend

* HTML5
* CSS3
* JavaScript (ES6)

---

## 📁 Project Structure

medical-chatbot-xai/
│
├── dataset/
│   ├── dataset.csv
│   ├── symptom_Description.csv
│   ├── symptom_precaution.csv
│   ├── Symptom-severity.csv
│
├── code/
│   ├── model.py
│   ├── app.py
│   ├── test.py
│   ├── index.html
│   ├── model.pkl
│   ├── label_encoder.pkl
│   ├── symptoms.pkl
│
└── README.md

---

## ⚙️ Installation Guide

### 🔧 Step 1: Install Python

Download and install Python from:
https://www.python.org/downloads/

✔ During installation:

* Check **“Add Python to PATH”**

---

### 🔧 Step 2: Verify Installation

Open terminal:

```bash
python --version
pip --version
```

---

### 🔧 Step 3: Install Required Libraries

Run:

```bash
pip install flask==2.3.3 flask-cors==4.0.0 pandas==2.0.3 numpy==1.24.4 scikit-learn==1.3.2 joblib==1.3.2 requests==2.31.0
```

---

### 🔧 Step 4: Project Setup

1. Download or clone the project
2. Extract dataset files into the `dataset` folder
3. Ensure folder structure matches the project structure

---

## 🚀 Running the Project

### ▶ Step 1: Train the Model

```bash
cd code
python model.py
```

✔ Output files generated:

* model.pkl
* label_encoder.pkl
* symptoms.pkl

---

### ▶ Step 2: Start Backend Server

```bash
python app.py
```

Server runs at:

http://127.0.0.1:5000

---

### ▶ Step 3: Open User Interface

Open:

index.html

(Double-click the file or open in browser)

---

## 🧪 How to Use

### ✔ Option 1: Direct Symptoms

```text
itching, skin_rash
```

### ✔ Option 2: Natural Language Input

```text
I have fever and headache
```

---

## 🔍 Key Features

### 🔽 Symptom Suggestions

* Displays matching symptoms as user types
* Reduces input errors

### 🧠 NLP Support

* Extracts symptoms from sentences
* Improves usability

### 📊 Confidence Score

* Shows reliability of prediction

### 💡 Explainable AI

* Explains which symptoms influenced prediction

---

## ⚙️ System Workflow

1. User inputs symptoms
2. Input is normalized and processed
3. Symptoms are converted into binary vector
4. Model predicts disease
5. Confidence score is calculated
6. Explanation is generated

---

## ⚠️ Limitations

* Works only with dataset-defined symptoms
* Cannot replace medical professionals
* Accuracy depends on data quality

---

## 🔮 Future Improvements

* Mobile application
* More advanced NLP models
* Real-time medical database integration
* Multi-language support

---

## 👨‍💻 Author

**Yusuf Aliyu**

---

## 📄 License

This project is for academic purposes only.

---

## 🎤 Presentation Summary

> “This system is a machine learning-based medical chatbot that predicts diseases from symptoms, provides confidence scores, and explains its predictions using explainable AI techniques.”

---

## ✅ Conclusion

This project demonstrates:

* Machine learning implementation
* Backend and frontend integration
* User-friendly design
* Practical AI application

---

**End of README**
