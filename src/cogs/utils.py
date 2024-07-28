import requests as r
import json
import os

jsfile="https://gist.github.com/v1s1t0r999/e209d7a7c847570b84a2803f22071819/"
url="https://api.github.com/gists"
token=os.getenv("token") 
headers={'Authorization':'token {}'.format(token)}
params={'scope':'gist'}


def getjson():
    con = r.get(f"{jsfile}/raw").json()
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
    payload={
            "description":f"splat dump - {num}",
            "public":True,
            "files":{
                "json":{"content": con}
                }
        }
    res=r.patch(url, headers=headers, params=params, data=json.dumps(payload))

