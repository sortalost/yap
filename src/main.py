from flask import Flask, render_template, redirect
import random
import json
from .cogs.utils import *
from .cogs import api


app = Flask(__name__)
app.register_blueprint(api.api)

@app.route("/")
def index():
    posts=getjson()
    return render_template("index.html",posts=posts)


@app.route("/post/<num>")
def post(num):
    try:
        post = getpost(num)
    except:
        return render_template("404.html")
    return render_template("post.html",name=post["name"],date=post["date"],time=post["time"],content=post["content"],img=post["img"])


@app.route("/random")
def rand():
    postcnt = len(getjson())
    return redirect(f"/post/{random.choice(range(1,postcnt+1))}")

@app.errorhandler(404)
def notfound(e):
    return render_template("404.html")


def initialize():
    with open("posts.json","r") as f:
        con = json.load(f)
    with open("/tmp/posts.json","w") as f:
        json.dump(con,f,indent=4)
    print("done initting")

if __name__=="__main__":
    initialize()
    app.run("0.0.0.0")

