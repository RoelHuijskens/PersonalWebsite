from flask import Flask, request, url_for, render_template, redirect,session
from datetime import timedelta
import yaml

import os

app = Flask(__name__)
app.secret_key = "3u834utn0m83um408vym92uc"





@app.route("/",methods=["POST", "GET"])
@app.route("/Home",methods=["POST", "GET"])
def login():
    return render_template("index.html")


@app.route("/<move>")
def SwitchMainPages(move):
    return render_template( move+ ".html")

@app.route("/Projects/<move>")
def SwitchProjectPages(move):
    print("Projects/"+move+"/html")
    return render_template("Projects/"+move+".html")









if __name__ == "__main__":
    app.run()