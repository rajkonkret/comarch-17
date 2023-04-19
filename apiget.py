# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/
from pprint import pprint

import requests as re

# pip install requests

response = re.get('http://api.nbp.pl/api/exchangerates/rates/B/EUR/')
response = re.get('http://api.nbp.pl/api/exchangerates/tables/A/')
print(response)

# 200 - ok
# 4... - błąd zapytania, np nie ma takiego adresu 404
# 5..  - bład serwera

table = response.json()
pprint(table)
# print(table['code'])
# print(table['rates'])
# print(table['table'])
# print(table['rates'][0])
# print(table['rates'][0]['no'])
# print(table['rates'][0]['effectiveDate'])
# print(table['rates'][0]['mid'])
pprint(table[0]['rates'])
# pydantic 