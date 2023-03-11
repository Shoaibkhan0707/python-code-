import requests
res=requests.get('https://iul.ac.in/')
type(res)
res.status_code==requests.codes.ok
print(res.text[:250])
