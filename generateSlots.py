

# def create():
    #headers = {'Authorization': f'Bearer {AIRTABLE_API_TOKEN}', 'Content-Type': 'application/json'}
    #url = f'https://api.airtable.com/v0/{BASE_ID}/{tableName}'

    #data = {
    #    "fields": {'AppointmentType': ['recDFrteJnzkwTIWK'], 'Start Time': "2024-07-26T16:30:00.000Z" }
    #}
    #response = requests.post(url, headers=headers, json=data)

    #if response.status_code == 200:
    #    print('New row created successfully!')
    #    return response.json()['id']
    #else:
    #    print(f'Failed to create row: {response.status_code}, {response.text}')
    #    return None

from dotenv import load_dotenv
import os, requests

load_dotenv()
BASE_ID = os.getenv('BASE_ID')
AIRTABLE_API_TOKEN = os.getenv('AIRTABLE_API_TOKEN')
tableName = 'Slots'

dates = ["2024-07-22","2024-07-23","2024-07-24","2024-07-25","2024-07-26"]
startTimes = ["T12:30:00.000Z", "T14:30:00.000Z","T16:30:00.000Z","T18:30:00.000Z","T20:30:00.000Z"]
endTimes = ["T13:30:00.000Z", "T15:30:00.000Z","T17:30:00.000Z","T19:30:00.000Z","T21:30:00.000Z"]
types = ['recDFrteJnzkwTIWK','recaadD9L8yBuKasZ','rec4Mpqh8WBMUtqjl','recdLSWHgaw1ftIzF','recq5FlEkZtM5rEEL','recPi2knZzdZPaPXz']

def create():
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_TOKEN}', 
        'Content-Type': 'application/json'
    }
    url = f'https://api.airtable.com/v0/{BASE_ID}/{tableName}'

    for date in dates:
        for startTime, endTime in zip(startTimes, endTimes):
            for type_id in types:
                data = {
                    "fields": {
                        'AppointmentType': [type_id], 
                        'Start Time': f'{date}{startTime}',
                        'End Time': f'{date}{endTime}',
                        'SlotCapacity': 1,
                        'SlotUsed': 0,
                        'SlotNote': "None"
                    }
                }
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    print('New row created successfully!')
                else:
                    print(f'Failed to create row: {response.status_code}, {response.text}')
    
    print("All Made Correctly")

create()
