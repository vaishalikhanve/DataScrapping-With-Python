import requests
import json
import os
url1="https://api.github.com/search/repositories?q=game+engine+language:java&sort=stars&order=desc"
url2="https://api.github.com/search/repositories?q=game+engine+language:c++&sort=stars&order=desc"
f1=open("datajava.json","w",encoding="utf-8")
f2=open("datac++.json","w",encoding="utf-8")
for l in range(2):
    if l==0:
        response=requests.get(url1)
    elif l==1:
        response=requests.get(url2)
    data=response.text
    parsed=json.loads(data)
    #print(json.dumps(parsed,indent=4))
    u2=parsed["items"]
    #print(json.dumps(u2,indent=4))
    for i in u2:
        k=i["url"]
        res=requests.get(k)
        da=res.text
        par=json.loads(da)
        if l==0:
            f1.write(json.dumps(par, indent=4))
        elif l==1:
            f2.write(json.dumps(par, indent=4))
        #print(json.dumps(par,indent=4))
        #print(par["git_url"])
        #os.system("git clone {}".format(par["git_url"]))
f2.close()
f1.close()

