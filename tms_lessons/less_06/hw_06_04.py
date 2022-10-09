import json
import csv

with open('dict.json',) as json_file:
    dict_from_json = json.load(json_file)

cols = ['id', 'Name', 'Age']
with open("dict.csv",'w') as csv_file:
    csv_reader = csv.DictWriter(csv_file, fieldnames=cols)
    csv_reader.writeheader()
    csv_reader.writerows(dict_from_json)
    headers=csv_reader.fieldnames
    print(headers)