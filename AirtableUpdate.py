import re
import csv, requests
import pandas as pd

BASE_ID = 'app03GWdFHFCFlo9u'
API_TOKEN = 'patMZxQ6JlBQ7YVUg.c111ec56ffecc8ff310f3db53ac7ff65f215fcbcd83550f7c4d7d38b3260fec5'


def main():

    csvPath = 'MasterDatabaseSchema_with_Keys_and_ExampleData.csv'
    
    cols = {}

    # loopCSV('Table', csvPath, cols)
    print(cols)
    loopCSV('Record', csvPath, cols)
        

def loopCSV(tableOrRecord, csvPath, cols):
    with open(csvPath) as f:
        reader = csv.reader(f)
        df = pd.read_csv(csvPath)
        row_count = len(df)

        i = 0
        currentTable = ''
        pastTable = ''
        fields = []
        records = []

        for row in reader:
            if i == 0:
                header = row
                i += 1
            elif i != 0:
                currentTable = row[0] # table name

                if tableOrRecord == "Table":
                    if i == row_count - 1:
                        cols[currentTable].append(row[1])
                        if row[3] == "Date":
                            fields.append(
                                {
                                    "name" : row[1],
                                    "type" : changeName(row[3], True),
                                    "options" : {"dateFormat" : {"name" : "local"}}
                                }
                            )
                        elif row[3] == "Checkbox":
                            fields.append(
                                {
                                    "name" : row[1],
                                    "type" : changeName(row[3], True),
                                    "options" : {"color" : "greenBright", "icon" : "check"}
                                }
                            )
                        elif row[3] == "Number":
                            fields.append(
                                {
                                    "name" : row[1],
                                    "type" : changeName(row[3], True),
                                    "options" : {"precision" : 0}
                                }
                            )                        
                        else:
                            fields.append(
                                {
                                    "name" : row[1],
                                    "type" : changeName(row[3], True)
                                }
                            )
                        createTable(fields, currentTable)

                    elif currentTable != pastTable: # create new table
                        cols[currentTable] = []
                        createTable(fields, pastTable) # creating a table of the past table
                        fields = [] # resetting
                        # print('reset')
                    
                    cols[currentTable].append(row[1])
                    if row[3] == "Date":
                        fields.append(
                            {
                                "name" : row[1],
                                "type" : changeName(row[3], True),
                                "options" : {"dateFormat" : {"name" : "local"}}
                            }
                        )
                    elif row[3] == "Checkbox":
                        fields.append(
                            {
                                "name" : row[1],
                                "type" : changeName(row[3], True),
                                "options" : {"color" : "greenBright", "icon" : "check"}
                            }
                        )
                    elif row[3] == "Number":
                        fields.append(
                            {
                                "name" : row[1],
                                "type" : changeName(row[3], True),
                                "options" : {"precision" : 0}
                            }
                        )
                    else:
                        fields.append(
                            {
                                "name" : row[1],
                                "type" : changeName(row[3], True)
                            }
                        )
                    

                elif tableOrRecord == "Record": 

                    if i == row_count - 1:
                        
                        records.append(
                            {
                                "fields" : {
                                    row[1] : row[5]
                                }
                            }
                        )
                        createRecord(records, currentTable)

                    elif currentTable != pastTable: # create new table
                        createRecord(records, pastTable)
                        records = [] # resetting
                        
                    records.append(
                        {
                            "fields" : {
                                row[1] : row[5]
                            }
                        }
                    )
                    
                pastTable = currentTable
                i += 1
            
def createTable(fields, tableName):
    if fields != []:
        data = {"fields" : fields, "name" : tableName}
        # print(data)
        headers = {'Authorization': f'Bearer {API_TOKEN}', 'Content-Type': 'application/json'}
        url = f'https://api.airtable.com/v0/meta/bases/{BASE_ID}/tables'
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code != 200:
            print(response.text)    
            print(data)


def createRecord(records, tableName):
    if records != [] and tableName != "Requirements":
        # print(records)
        data = {"records" : records}
        headers = {'Authorization': f'Bearer {API_TOKEN}', 'Content-Type': 'application/json'}
        url = f'https://api.airtable.com/v0/{BASE_ID}/{tableName}'
        
        for i in range(0, len(records), 10):
            batch = records[i:i+10]
            data = {"records": batch}
            response = requests.post(url, json=data, headers=headers)
            
            if response.status_code != 200:
                print(response.text)    
                print(data)
       

def changeName(input_string, capitalCase: bool):
    # Remove text within parentheses
    input_string = re.sub(r'\([^)]*\)', '', input_string)
    
    # Convert to CapitalCase
    input_string = input_string.title()
    
    # Remove leading and trailing whitespace
    input_string = input_string.strip()
    
    # Replace spaces with empty string
    input_string = input_string.replace(" ", "")


    if capitalCase == True:
        input_string = input_string[0].lower() + input_string[1:]

    
    return input_string



main()