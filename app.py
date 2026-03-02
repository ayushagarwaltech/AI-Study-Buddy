from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import numpy as np
import os
import random
from transformers import pipeline

app = Flask(__name__)
app.secret_key = "studybuddy_secret_key"

# Load ML Model
model_path = os.path.join("model", "student_model.pkl")
model = pickle.load(open(model_path, "rb"))

# Load Tiny AI Models
print("Loading Tiny AI models...")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6")
text_generator = pipeline("text-generation", model="distilgpt2")
print("AI Models Ready!")

quiz_results = []

# 10+ Quiz Subjects
question_bank = {
    "Python": [{"question": "Keyword to define function?", "options": ["def","func","define","lambda"], "answer":"def"}],
    "Machine Learning": [{"question":"Regression algorithm?","options":["KNN","Linear Regression","K-Means","SVM"],"answer":"Linear Regression"}],
    "Data Science":[{"question":"Library for data analysis?","options":["NumPy","Pandas","Flask","Bootstrap"],"answer":"Pandas"}],
    "Deep Learning":[{"question":"DL framework?","options":["TensorFlow","HTML","CSS","Excel"],"answer":"TensorFlow"}],
    "Statistics":[{"question":"Mean measures?","options":["Variance","Central Tendency","Skewness","Range"],"answer":"Central Tendency"}],
    "Operating Systems":[{"question":"Linux is?","options":["Kernel","Browser","IDE","DB"],"answer":"Kernel"}],
    "DBMS":[{"question":"SQL is used for?","options":["Styling","Querying","Compiling","Design"],"answer":"Querying"}],
    "Computer Networks":[{"question":"HTTP stands for?","options":["Hyper Text Transfer Protocol","High Text Transfer","Hyper Transfer","None"],"answer":"Hyper Text Transfer Protocol"}],
    "Artificial Intelligence":[{"question":"AI means?","options":["Artificial Intelligence","Auto Input","Advanced Info","None"],"answer":"Artificial Intelligence"}],
    "Java":[{"question":"Java is?","options":["Compiled","Interpreted","Both","None"],"answer":"Both"}]
}

@app.route("/", methods=["GET","POST"])
def login():
    if request.method=="POST":
        u=request.form["username"]
        p=request.form["password"]
        if u=="demo" and p=="demo123":
            session["user"]=u
            session["role"]="student"
            return redirect("/dashboard")
        elif u=="admin" and p=="admin123":
            session["user"]="Admin"
            session["role"]="admin"
            return redirect("/admin")
        else:
            return render_template("login.html",error="Invalid Credentials")
    return render_template("login.html")

@app.route("/guest")
def guest():
    session["user"]="Guest"
    session["role"]="student"
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    predicted_score=None
    recommendation=None

    if request.method=="POST":
        hours=float(request.form["hours"])
        attendance=float(request.form["attendance"])
        previous=float(request.form["previous"])

        predicted_score=model.predict([[hours,attendance,previous]])[0]

        if predicted_score<50:
            recommendation="Need improvement."
        elif predicted_score<75:
            recommendation="Good progress."
        else:
            recommendation="Excellent performance."

    user_results=[r for r in quiz_results if r["username"]==session.get("user")]
    total_attempts=len(user_results)
    average_score=round(sum(r["score"] for r in user_results)/total_attempts,2) if total_attempts>0 else 0
    best_score=max([r["score"] for r in user_results],default=0)

    return render_template("dashboard.html",
                           user=session.get("user"),
                           predicted_score=predicted_score,
                           recommendation=recommendation,
                           total_attempts=total_attempts,
                           average_score=average_score,
                           best_score=best_score)

@app.route("/quiz",methods=["GET","POST"])
def quiz():
    if request.method=="POST":
        subject=request.form["subject"]
        questions=question_bank[subject]
        session["quiz_subject"]=subject
        session["quiz_questions"]=questions
        return render_template(
            "quiz.html",
            subject=subject,
            questions=questions,
            question_bank=question_bank
        )
    return render_template(
        "quiz.html",
        subject=None,
        question_bank=question_bank
    )

@app.route("/submit_quiz",methods=["POST"])
def submit_quiz():
    questions=session.get("quiz_questions")
    subject=session.get("quiz_subject")
    score=0
    for i,q in enumerate(questions):
        if request.form.get(f"q{i}")==q["answer"]:
            score+=1
    quiz_results.append({"username":session["user"],"subject":subject,"score":score})
    weakness="Revise topic." if score==0 else "Good understanding."
    return render_template("result.html",score=score,subject=subject,weakness=weakness)

@app.route("/admin")
def admin():
    if session.get("role")!="admin":
        return redirect("/")
    return render_template("admin.html",results=quiz_results)

# AI ROUTES
@app.route("/ai_tools")
def ai_tools():
    return render_template("ai_tools.html")

@app.route("/explain_topic",methods=["POST"])
def explain_topic():
    topic=request.form["topic"]
    result=text_generator(f"Explain {topic} simply:",max_length=150)
    return render_template("ai_tools.html",explanation=result[0]['generated_text'])

@app.route("/summarize_notes",methods=["POST"])
def summarize_notes():
    notes=request.form["notes"]
    summary=summarizer(notes,max_length=100,min_length=30,do_sample=False)
    return render_template("ai_tools.html",summary=summary[0]['summary_text'])

@app.route("/generate_flashcards",methods=["POST"])
def generate_flashcards():
    topic=request.form["flash_topic"]
    result=text_generator(f"Create 5 flashcards about {topic}:",max_length=200)
    return render_template("ai_tools.html",flashcards=result[0]['generated_text'])

if __name__=="__main__":

    app.run(debug=True)
