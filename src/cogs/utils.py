import requests as r
import json
import os

jsfile="https://gist.github.com/v1s1t0r999/c505d338345f02e3036f851346f8a7a4"
url="https://api.github.com/gists/"
gist="c505d338345f02e3036f851346f8a7a4"
token=os.getenv("token") 
headers={'Authorization':'token {}'.format(token)}
params={'scope':'gist'}


def getpost(fn="1"):
    con = r.get(f"{jsfile}/raw/{fn}").json()
    return con

def gistfiles():
    try:
        res = r.get(url+gist).json()
        file_count = len(res.get('files', {}))
        return file_count
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def addpost(name, date, time, content, img):
    num = str(gistfiles()+1)
    con = {
        "num":num,
        "name":name,
        "date":date,
        "time":time,
        "content":content,
        "img": img
    }
    payload={
            "description":f"splat dump - {num}",
            "public":True,
            "files":{
                num:{"content": json.dumps(con)}
                }
        }
    res=r.patch(url+gist, headers=headers, params=params, data=json.dumps(payload,indent=4))

    print(res.text)
    return str(num)

