
import requests
import json

url = "https://api.telegram.org/bot5270788758:AAF0N5nfEjlynElbiCuQwr-DZWJMsschP3w/sendDocument?chat_id=395490182"

x=['f1.txt','f2.txt']
for i in x:
    files = {'document': open(i, 'rb')}
    r = requests.post(url, files=files)
    print(r.status_code)