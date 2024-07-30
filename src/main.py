from flask import Flask, render_template, redirect, url_for, request, session
import random
import json
import os
from .cogs.utils import *
from .cogs import api


app = Flask(__name__)
app.secret_key("smd")
app.register_blueprint(api.api)
username=os.getenv("username")
password=os.getenv("password")


def check_login():
    if not 'logged_in' in session:
        session["logged_in"]=False
    return session["logged_in"]


@app.route("/")
def index():
    posts=getjson()
    return render_template("index.html",posts=posts,session=session)


@app.route("/docs")
def docs():
    return render_template("docs.html",session=session)

@app.route("/post/<num>")
def post(num):
    try:
        post = getpost(num)
    except:
        return render_template("404.html")
    return render_template("post.html",name=post["name"],date=post["date"],time=post["time"],content=post["content"],img=post["img"],session=session)


@app.route("/post")
def onlypost():
    return redirect(url_for("rand"))


@app.route("/new",methods=["GET","POST"])
def addnew():
    if session['logged_in']==False:
        return "not logged in" #redirect to login
    if request.method=="GET":
        return render_template("new.html",session=session)
    name = request.form["title"]
    date=post.get("date") or datetime.now().strftime("%B %d, %Y").lower()
    time=post.get("time") or datetime.now().strftime("%H.%M %p").lower()
    content = request.form["content"]
    img="https://random.imagecdn.app/400/210"
    num = addpost(name,date,time,content)
    return redirect(f"/post/{num}")


@app.route("/random")
def rand():
    postcnt = len(getjson())
    return redirect(f"/post/{random.choice(range(1,postcnt+1))}")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if check_login()==True:
        return "already logged in"
    error = None
    if request.method == 'POST':
        if request.form['username'] != username or request.form['password'] != password:
            error = 'Invalid.'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error,session=session)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.errorhandler(404)
def notfound(e):
    return render_template("404.html",session=session)

@app.before_request
def b4req():
    c = check_login()
    print(c)

if __name__=="__main__":
    app.run("0.0.0.0")

