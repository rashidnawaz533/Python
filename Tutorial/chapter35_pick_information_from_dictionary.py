"""
The name of the list of dictionaries is custs.
Target the dictionary with an index of 0 and store it in the variable target_dict.
"""
custs = [{}]
target_dict = custs[0]

"""
The line below targets a dictionary in a list of dictionaries. 
Code the line that targets the value paired with the key "name" in that dictionary. 
Make up the variable that stores the value.
x = y[33]
"""
y={0: {'name': ''},}
x = y[0]
z = x['name']

"""
Target one of the dictionaries in the list, loading it into a variable. Then target a value within that dictionary, 
loading it into another variable. Display the value.
"""
customers = [
  {
    "customer id": 0,
    "first name":"John",
    "last name": "Ogden",
    "address": "301 Arbor Rd.",
  },
  {
    "customer id": 1,
    "first name":"Ann",
    "last name": "Sattermyer",
    "address": "PO Box 1145",
  },
  {
    "customer id": 2,
    "first name":"Jill",
    "last name": "Somers",
    "address": "3 Main St.",
  },
]

customer = customers[1]
firstname = customer['first name']
print(firstname)