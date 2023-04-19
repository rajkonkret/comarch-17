import json
from pprint import pprint

with open('dane_json.json', 'r') as f:
    data = json.load(f)

pprint(data)
pprint(data['members'])
pprint(data['members'][0]['powers'][1])