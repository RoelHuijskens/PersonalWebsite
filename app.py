from flask import Flask, request, url_for, render_template, redirect,session
from datetime import timedelta
import yaml

import os

app = Flask(__name__)
app.secret_key = "3u834utn0m83um408vym92uc"





@app.route("/",methods=["POST", "GET"])
@app.route("/Home",methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("radiobuttonQuestion"))
    else:
        return render_template("index.html")


@app.route("/<move>")
def SwitchMainPages(move):
    return render_template( move+ ".html")

@app.route("/Projects/<move>")
def SwitchProjectPages(move):
    print("Projects/"+move+"/html")
    return render_template("Projects/"+move+".html")





@app.route("/CheckQuestion/",methods= ["GET","POST"])
def CheckBoxQuestion():
    question_index = 'Question_'+ str(Current_question)
    if request.method == "POST":
        Question_tag = Questions_yaml['content'][question_index]['Question_tag']
        delta = request.form['satnav']
        session[Question_tag] = request.form[Question_tag]

        return redirect(url_for("next_question",delta = delta))
    else:
        question_index = 'Question_'+ str(Current_question)
        Question_options =  Questions_yaml['content'][question_index]['Question_Options']
        Question_text =  Questions_yaml['content'][question_index]['Question_Text']
        Question_tag = Questions_yaml['content'][question_index]['Question_tag']
        
        return render_template("CheckBox.html",Questionlist = Question_options, QuestionTag = Question_tag, Question_text = Question_text)





@app.route("/RadioQuestion/",methods= ["GET","POST"])
def radiobuttonQuestion():
    question_index = 'Question_'+ str(Current_question)
    if request.method == "POST":
        Question_tag = Questions_yaml['content'][question_index]['Question_tag']
        delta = request.form['satnav']
        session[Question_tag] = request.form[Question_tag]

        return redirect(url_for("next_question",delta = delta))
    else:
        question_index = 'Question_'+ str(Current_question)
        Question_options =  Questions_yaml['content'][question_index]['Question_Options']
        Question_text =  Questions_yaml['content'][question_index]['Question_Text']
        Question_tag = Questions_yaml['content'][question_index]['Question_tag']
        
        return render_template("RadioBox.html",Questionlist = Question_options, QuestionTag = Question_tag, Question_text = Question_text)


def switch_question(delta):
    global Current_question
    if Current_question + delta >= 0 & Current_question + delta < len(Questions_yaml['content']):
        Current_question += delta
    return Current_question




if __name__ == "__main__":
    app.run()