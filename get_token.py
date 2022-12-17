import requests
import json
import re

def func():
  
  url = "https://dev.salestrekker.com/graphql"

  payload = json.dumps({
    "query": "mutation{\n  authenticate(email:\"test1@wavesfinancial.com.au\" password:\"Password1$$\") {\n    token\n  }\n}\n"
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
  print(token)
  return 0

func()
