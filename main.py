from flask import Flask, request, render_template, url_for, redirect
from jinja2 import Environment, FileSystemLoader



app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template('start_res.html')

@app.route("/q1/")
def question1():
    return render_template('question.html')

@app.route("/q2/")
def question2():
    return render_template('question.html')

@app.route("/q3/")
def question3():
    return render_template('question.html')

@app.route("/q4/")
def question4():
    return render_template('question.html')

@app.route("/q5/")
def question5():
    return render_template('question.html')

@app.route("/resA/")
def resultA():
    return render_template('result.html')

@app.route("/resB/")
def resultB():
    return render_template('result.html')

@app.route("/resC/")
def resultC():
    return render_template('result.html')

@app.route("/resD/")
def resultD():
    return render_template('result.html')

