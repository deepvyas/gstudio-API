import requests
import json

url = "http://localhost:8000/jrpc_test/"
headers = {'content-type':'application/json'}

payload1 = {'jsonrpc':'2.0','id':0,'method':'save','params':['Deep','Vyas','Smart']}

payload2 = {'jsonrpc':'2.0','id':0,'method':'fetch','params':[]}

r1 = requests.post(url,data=json.dumps(payload1),headers=headers).json()

print r1

r2 = requests.post(url,data=json.dumps(payload2),headers=headers).json()

print r2