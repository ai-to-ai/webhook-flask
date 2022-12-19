import requests
import json
import re
import config
def func():
  try:
    print('Get Token')
    url = "https://dev.salestrekker.com/graphql"
    print(config.BROKERENGINE['user'])
    payload = json.dumps({
      "query": "mutation{\n  authenticate(email:\""+config.SALESTREKKER['user']+"\" password:\""+config.SALESTREKKER["pass"]+"\") {\n    token\n  }\n}\n"
    })
    headers = {
      'Accept-Encoding': 'gzip, deflate, br',
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Connection': 'keep-alive',
      'DNT': '1',
      'Origin': 'https://dev.salestrekker.com'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    token = re.findall(r'"token":"(.*)"', response.text)[0]
    with open('token.txt','w') as f:
      f.write(token)
      f.close()

  except Exception as e:
    print(e)
