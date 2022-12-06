import requests,json

# url="https://api.telegram.org/bot5270788758:AAF0N5nfEjlynElbiCuQwr-DZWJMsschP3w/getUpdates?offset=-1"
url="https://api.telegram.org/bot5270788758:AAF0N5nfEjlynElbiCuQwr-DZWJMsschP3w/getUpdates"
param={'offset':'-1'}
links = requests.get(url, params=param,verify=False,stream=True)

print(links.history)





# getText = links.text
# data = json.loads(getText)

# x=data['result'][0]['message']['text']
# print(x)