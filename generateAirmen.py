from dotenv import load_dotenv
import os, requests, time

load_dotenv()
BASE_ID = os.getenv('BASE_ID')
AIRTABLE_API_TOKEN = os.getenv('AIRTABLE_API_TOKEN')
tableName = 'Members'

def create():
    headers = {'Authorization': f'Bearer {AIRTABLE_API_TOKEN}', 'Content-Type': 'application/json'}
    url = f'https://api.airtable.com/v0/{BASE_ID}/{tableName}'

    data = {
        "fields": {}
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print('New row created successfully!')
        return response.json()['id']
    else:
        print(f'Failed to create row: {response.status_code}, {response.text}')
        return None

def check(id):    
    headers = {'Authorization': f'Bearer {AIRTABLE_API_TOKEN}', 'Content-Type': 'application/json'}
    url = f'https://api.airtable.com/v0/{BASE_ID}/{tableName}/{id}'

    response = requests.get(url, headers=headers)
    
    try: 
        # print(response.json()['fields'])
        return response.json()['fields']['Profile Photo Created?']
    except:
        return False
        

def main():
    numAirmen = int(input('Enter the number of airmen to generate: '))
    
    for _ in range(numAirmen):
        loaded = False
        id = create()
        if not id:
                print('Failed to create row')
                break
        while not loaded:
            # print(loaded)
            loaded = check(id)
            time.sleep(5)
main()