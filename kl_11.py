import pickle
from kl_10 import Person

with open('data.pickle', 'rb') as file:
    p = pickle.load(file)

for person in p:
    print(type(person))
    person.greet()

with open('data.txt', 'r') as f:
    p_2 = f.read()

print(type(p_2))
print(p_2)