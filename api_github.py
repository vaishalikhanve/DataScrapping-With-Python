import requests
import json
import os
url1="https://api.github.com/search/repositories?q=game+engine+language:java&sort=stars&order=desc&page="
url2="https://api.github.com/search/repositories?q=game+engine+language:c++&sort=stars&order=desc&page="
f1=open("datajava.json","w",encoding="utf-8")
f2=open("datac++.json","w",encoding="utf-8")
flag=0
for l in range(68):
    if l==34:
        flag=1
    if flag==0:
        url=url1+str(l+1)
        print(url)
    elif flag==1:
        url=url2+str(l-33)
    response=requests.get(url)
    data=response.text
    parsed=json.loads(data)
    u2=parsed["items"]
    for i in u2:
        k=i["url"]
        res=requests.get(k)
        da=res.text
        par=json.loads(da)
        if flag==0:
            f1.write(json.dumps(par,indent=4))
        else:
            f2.write(json.dumps(par,indent=4))           
f2.close()
f1.close()

