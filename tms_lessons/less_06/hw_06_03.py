import json


name_age_dict=[{'id': '123451' , 'Name' : 'John', 'Age':13},
{'id': '123452' , 'Name' : 'Jojo', 'Age':14},
{'id': '123453' , 'Name' : 'Kevin', 'Age':23},
{'id': '123454' , 'Name' : 'Lara', 'Age':18},
{'id': '123455' , 'Name' : 'Kevin', 'Age':67},
{'id': '123456' , 'Name' : 'Don', 'Age':55}
]

with open('dict.json', 'w') as json.save:
    json.dump(name_age_dict, json.save)