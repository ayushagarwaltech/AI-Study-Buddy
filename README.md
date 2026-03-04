# 🎓 AI Study Buddy – Intelligent Learning & Performance Prediction System

## 📌 Project Overview

AI Study Buddy is a web-based intelligent learning platform that helps students:

* 📊 Predict final exam scores using Machine Learning
* 📝 Attempt subject-wise quizzes
* 🤖 Use AI tools for topic explanation, summarization, and flashcard generation
* 📈 Track quiz performance and progress

The system integrates Machine Learning, AI models, and a Flask-based web application to provide a smart and interactive study experience.

---

## 🚀 Features

### 🔹 Student Features

* Final score prediction using Linear Regression
* Personalized performance feedback
* Subject-wise quiz system
* AI-powered topic explanation
* Automatic notes summarization
* Flashcard generation
* Performance dashboard with statistics

### 🔹 Admin Features

* View all quiz results
* Monitor student performance

---

## 🛠️ Technologies Used

### 🔹 Frontend

* HTML5
* Tailwind CSS
* JavaScript
* Chart.js (Data Visualization)

### 🔹 Backend

* Python
* Flask Framework

### 🔹 Machine Learning

* Scikit-learn (Linear Regression)
* NumPy
* Pandas

### 🔹 AI Models

* HuggingFace Transformers
* DistilBART (Summarization Model)
* DistilGPT2 (Text Generation Model)

### 🔹 Model Storage

* Pickle (.pkl file)

---

## 📂 Project Structure

```
AI-Study-Buddy/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── train_model.py
│   └── student_model.pkl
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── quiz.html
│   ├── result.html
│   ├── admin.html
│   ├── ai_tools.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/ayushagarwaltech/AI-Study-Buddy.git
cd AI-Study-Buddy
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train the Model (First Time Only)

```
python model/train_model.py
```

### 4️⃣ Run the Application

```
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🔑 Demo Login Credentials

### 👨‍🎓 Student Login

* Username: demo
* Password: demo123

### 👨‍💼 Admin Login

* Username: admin
* Password: admin123

---

## 📊 Machine Learning Model

The system uses a Linear Regression model trained on:

* Hours Studied
* Attendance
* Previous Score

Based on predicted score:

* Below 50 → Need Improvement
* 50–75 → Good Progress
* Above 75 → Excellent Performance

---

## 🤖 AI Tools Included

* Topic Explanation Generator
* Notes Summarizer
* Flashcard Generator

These tools use pre-trained transformer models to generate intelligent responses.

---

## 📌 Future Enhancements

* Database integration (MySQL / SQLite)
* User registration system
* Cloud deployment
* Advanced ML models
* Secure authentication system

---

## 👨‍💻 Developed For

Academic Project – AI Study Buddy

---

## ✅ Conclusion

AI Study Buddy successfully integrates Machine Learning and AI tools into a web-based learning platform.

The system predicts student performance and enhances learning through quizzes, summarization, and intelligent content generation.

This project demonstrates how AI can be effectively applied in the education domain to support smarter and personalized learning.

