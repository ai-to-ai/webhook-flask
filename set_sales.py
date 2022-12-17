import json
import requests

def main():
    BrokerEngineID = input_data['BrokerEngineID']

    variable1 = "THIS IS THE DEAL ID GOT FROM THE CUSTOM FIELD 1 FROM BROKER ENGINE"
    variable2 = "THIS IS THE TOKEN GOT EARLIER FROM THE AUTHENTICATION"
    variable3 = "THIS IS THE ID FROM THE JSON TABLE THAT MATCHED (SALESTREKKER ID)"
    ticketValue = input_data['ticketValue']

    if input_data['BTicketLabel']:
        BTicketLabel = input_data['BTicketLabel']
    else:
        BTicketLabel = ""


    url = "https://sfg.salestrekker.com/graphql"

    payload = "{\"query\":\"query{ticket(id:\\\"" + variable1 + "\\\"){id name idLabels idOwner idWorkflow idStage idClients ticketClientTypes {idContact idLabel} name values {onceOff}}}\",\"variables\":{}}"

    headers = {
        'Authorization': 'Bearer ' + variable2,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    y = json.loads(response.text)


    ticketID = variable1
    idOwner = y['data']['ticket']['idOwner']
    idWorkflow = "THIS IS THE ID WORKFLOW FROM EARLIER"
    idStage = input_data['variable8']
    idLabels = y['data']['ticket']['idLabels']
    idClients = y['data']['ticket']['idClients']
    ticketClientTypes = y['data']['ticket']['ticketClientTypes']
    idName = y['data']['ticket']['name']
    idValues = y['data']['ticket']['values']


    leadLabel = BTicketLabel

    if leadLabel not in idLabels:
        idLabels.insert(0, leadLabel)

    idLabelsString_str1 = "\"" + "\" \"".join(map(str, idLabels)) + "\""
    idLabelsString = idLabelsString_str1
    idClientsString_str1 = "\"" + "\" \"".join(map(str, idClients)) + "\""
    ticketClientTypes_str1 = json.dumps(ticketClientTypes, sort_keys=True, indent=0)


    BrokerEngineIDString = "{BrokerEngineID:" + BrokerEngineID + "}"

    ss = "["

    for a in ticketClientTypes:
        ss += "{"
        if a.get("idContact"):
            ss += "idContact: \"" + a.get("idContact", '') + "\""
        label = a.get("idLabel")
        if label:
            ss += " idLabel: \"" + a.get("idLabel", '') + "\""
        else:
            # ss += " idLabel: "
            pass
        ss += "}"
    ss += "]"


    payload2 = payload2.format(ticketID, idOwner, idWorkflow, idStage, idLabelsString, idClientsString_str1, str(ss), idName, ticketValue, BrokerEngineIDString )
    print(payload2)


    d = {
        'query': payload2,
        'variables': '{}'
    }
    res = requests.request('POST', 'https://dev.salestrekker.com/graphql', headers=headers,
                           json=d)


    print(res.status_code)
    print(res.content)

