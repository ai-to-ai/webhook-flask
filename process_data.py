import requests
import json

def main(data):
    try:
        print('Process Data')
        brokerengine_webhook_application_name = data['application_name']
        brokerengine_webook_application_purpose = data['application_purpose']
        holding_options_variable = ''
        ticketLabel = ''
        brokerengine_webook_application_base_loan_amount = data['application_base_loan_amount']
        ticketValue = '1'
        brokerengine_webhook_application_stage = data['application_stage']


        if brokerengine_webook_application_base_loan_amount: #(not null or empty)
            ticketValue = int(float(brokerengine_webook_application_base_loan_amount))

        words = set(brokerengine_webhook_application_name.split())
        if 'Purchase' in words:
            if brokerengine_webook_application_purpose == 'Owner Occupier':
                print('purchase owner occ')
                holding_options_variable = '1'
                ticketLabel = 'a3f1edff-2095-4bd1-9f23-ff862088f1dc'
                
            if brokerengine_webook_application_purpose == 'Investment':
                print('purchase investment')
                holding_options_variable = '2'
                ticketLabel = '7b56af00-8b81-4753-94c5-31ccabd13b7c'

        if 'Refinance' in words:
            if brokerengine_webook_application_purpose == 'Owner Occupier':
                print ('refinance owner occ')
                holding_options_variable = '3'
                ticketLabel = '3142e1f3-cce2-41bd-b22c-6acae87bc8c1'

            if brokerengine_webook_application_purpose == 'Investment':
                print ('refinance investment')
                variable4 = '4'
                ticketLabel = '3142e1f3-cce2-41bd-b22c-6acae87bc8c1'


        if brokerengine_webhook_application_stage == 'Settlement':
            ticketLabel = '2cb2d4ce-24ce-42ae-9a0a-834026bbe313'

        if brokerengine_webhook_application_stage == 'Lost/Declined':
            ticketLabel = ''

        if len(ticketLabel) == 0:
            ticketLabel = 'bd8cae51-9f03-41c6-82a0-75d078b830f6'


        output = {'ticketLabel': ticketLabel,'ticketValue' : ticketValue}
        return output   
    except Exception as e:
        print(e)
        return ""
    