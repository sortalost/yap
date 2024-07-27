from flask import Flask, render_template
from .utils import *

app = Flask(__name__)

@app.route("/")
def one():
    posts=getjson()
    return render_template("one.html",posts=posts)

@app.route("/new")
def newpost():
    return render_template("two.html")

@app.route("/post/<num>")
def post(num):
    try:
        post = getpost(num)
    except:
        return render_template("404.html")
    return render_template("post.html",name=post["name"],date=post["date"],time=post["time"],content=post["content"],img=post["img"])

@app.errorhandler(404)
def notfound(e):
    return render_template("404.html")

if __name__=="__main__":
    app.run("0.0.0.0")

