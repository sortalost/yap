from flask import Blueprint
from flask import request, render_template, redirect, url_for, session
from .utils import addpost, getpost, getjson
from datetime import datetime

api = Blueprint('api', __name__, url_prefix="/api")


@api.route("/new",methods=["POST"])
def new():
    if session['logged_in'] is False:
        return {"error":"log in to access. check your environment variable in vercel"}
    post = request.get_json(force=True)
    name=post.get("name")
    date=post.get("date") or datetime.now().strftime("%B %d, %Y").lower()
    time=post.get("time") or datetime.now().strftime("%H.%M %p").lower()
    content=post.get("content")
    img=post.get("img") or "https://random.imagecdn.app/400/210"
    if name is None:
        return {"error":"name field is required"}
    if content is None:
        return {"error":"content field is required"}
    num = addpost(name, date, time, content, img)
    return {"id":num}

@api.route("/get")
def get():
    num = request.args.get("id")
    if num is None:
        return getjson()
    return getpost(num)

