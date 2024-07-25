from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/start")
def start_test(): # 點擊start, 開始遊戲 進入/question1

    return render_template('start.html')


@app.route("/question1")
def question1():



@app.route("/question2")
def question2():



@app.route("/question3")
def question3():


@app.route("/question4")
def question4():


@app.route("/question5")
def question5():


@app.route("/result")
def result():


