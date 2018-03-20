import requests
import json
firebase_url = 'https://hydro-2018.firebaseio.com/'

for i in range(0,100):
    data = {'value': i}
    result = requests.post(firebase_url + '/value.json', data=json.dumps(data))
    print(i)
