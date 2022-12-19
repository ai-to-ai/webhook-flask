import json
import requests
import config
import sys
import os
import linecache

def main(data, ticketData, workflow):
    try:
        BrokerEngineID = data['application_id']

        variable1 = data['application_custom_text1'] or ""
        with open('token.txt', 'r') as f:
            token = f.read()
            f.close()
        variable2 = token
        stages = workflow['data']['workflow']['stages']
        try:
            stage_name = data['application_stage']
            print(stage_name)
            sfg_stage = [i for i in config.SFG_CHECKER if i["BROKER_STAGE"] == stage_name][0]
            variable3 = sfg_stage['SFG_ID']
        except Exception as e:
            print(e)
            variable3 = ""
        ticketValue = ticketData['ticketValue']

        if ticketData['ticketLabel']:
            BTicketLabel = ticketData['ticketLabel']
        else:
            BTicketLabel = ""
        print(variable1)
        print(variable2)
        print(variable3)
        url = "https://sfg.salestrekker.com/graphql"

        payload = "{\"query\":\"query{ticket(id:\\\"" + variable1 + "\\\"){id name idLabels idOwner idWorkflow idStage idClients ticketClientTypes {idContact idLabel} name values {onceOff}}}\",\"variables\":{}}"

        headers = {
            'Authorization': f'Bearer {variable2}',
            'Content-Type': 'application/json'
        }
        print(payload)
        print(headers)
        response = requests.request("POST", url, headers=headers, data=payload)

        y = json.loads(response.text)

        print(response.text)
        print(response)
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
    except Exception as e:
        print('------')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_tb.tb_lineno)
        print(e)
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))


