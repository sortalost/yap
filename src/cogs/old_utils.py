"""
This file is used for a server with a filetype system.
rename this to "utils.py" and the other one to anything else when using on pc
"""

import json

jsfile="posts.json"

def makefile():
    f = open(jsfile,"w")
    f.write("{}")
    f.close()

def getjson():
    with open(jsfile,"r") as f:
        con = json.load(f)
    return con

def getpost(num:str):
    con = getjson()
    post = con[num]
    return post

def addpost(name, date, time, content, img):
    con = getjson()
    num = str(len(con)+1)
    con.update({num:
        {
        "num":num,
        "name":name,
        "date":date,
        "time":time,
        "content":content,
        "img": img
        }
    })
    with open(jsfile, "w") as f:
        json.dump(con,f,indent=4)
    return num
