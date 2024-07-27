import json

def getjson():
    with open("posts.json","r") as f:
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
    with open("posts.json", "w") as f:
        json.dump(con,f,indent=4)
    return num
