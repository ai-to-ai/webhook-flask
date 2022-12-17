import requests
import json

def main():
  url = "https://dev.salestrekker.com/graphql"

  payload = json.dumps({
    "query": "query {\n  workflow(id:\"b0cc73ee-4917-4b54-8e1b-eafc571da7a6\") {\n    id\n    name\n    stages {\n      name\n      id\n    }\n  }\n}\n"
  })
  headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://dev.salestrekker.com',
    'authorization': 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjE5ZGUzMzQ1LWE4NzctNGQ5Ni1iMGQ3LTE5NGVkMTc4OGYwNCIsImlkQ3VycmVudE9yZ2FuaXphdGlvbiI6ImEzZDY0MTA1LWY4OGUtNDQxYi1hMWQ2LTI0YTRlZmU5YzYzYiIsImlzQWRtaW5pc3RyYXRvciI6ZmFsc2UsImlzQnJva2VyIjp0cnVlLCJpc01lbnRvciI6ZmFsc2UsImlhdCI6MTY3MTA3Mjk4NiwiZXhwIjoxNjcyMjgyNTg2fQ.Oc_4CPqlmvvpp0G3SvOEARYBO1vKR9Ne8bHWCgrFJ0Q'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
