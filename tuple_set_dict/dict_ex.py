# creating a dictionary 
a={'Name':'Shivi','Age':29,'Class':'Premium'}
print(a)

#! Getting all the keys from dictionary 
print(a.keys())
#* use list(a.keys()) to display as list.

#! getting all the values from dict 
print(a.values())

#! getting all the items from dict as a list of tuples.
print(a.items())

#? Nested Dict 
b={'fruits':{'apple':'5kg','custard apple':'3kg'},'vegetables':{'cabbage':'1kg','tomato':'500g'}
,'cereals':{'rice':'1kg','wheat':'2kg'}}

from pprint import pp
pp(b)

#! accessing a value from dict 
print(a['Name'])
print(a['Class'])

#print(a['city]) #keyError:'City'

#! accessing a value from dict using get() 
print(a.get('Name'))
print(a.get('Class'))
print(a.get('City')) #None
print(a.get('City','Not Found'))

#! default value can be specified
print(a.get('Name','Not found'))

#* Traversing a dict 
#! Style 1
for key in a:
    print(f'style 1--> {key,a[key]}')

#! Style 2
for key,value in a.items():
    print(f'style 2--> {key,value}')

#! Only values 
for value in a.values():
    print (f'values--> {value}')

#! Only keys 
for key in a.keys():
    print(f'keys--> {key}')