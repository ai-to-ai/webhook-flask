import requests
import json
import config


def main():
  try:
    url = "https://dev.salestrekker.com/graphql"

    WORKFLOW_ID = config.WORKFLOW_ID

    with open('token.txt','r') as f:
      TOKEN = f.read()

    payload = json.dumps({
      "query": "query {\n  workflow(id:\""+WORKFLOW_ID+"\") {\n    id\n    name\n    stages {\n      name\n      id\n    }\n  }\n}\n"
    })
    headers = {
      'Accept-Encoding': 'gzip, deflate, br',
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Connection': 'keep-alive',
      'DNT': '1',
      'Origin': 'https://dev.salestrekker.com',
      'authorization': f'bearer {TOKEN}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return data
  except Exception as e:
    print(e)
    return ""
  
