"""
Loop through the keys of a dictionary. Display each key. Make everything up.
"""

list = {0:'1',1:'2',4:'6'}
for key in list.keys():
 print(key)

 """
 Loop through the keys in a dictionary and display the value for each key. Make everything up.
 """
 for key in list.keys():
  print(list[key])

 """
 Loop through a dictionary's keys. Append the value of each key to a list. Make everything up.
 """
newlist = []
for key in list.keys():
  newlist.append(list[key])

print(newlist)

"""
Loop through a dictionary's keys. If a key's value is greater than or equal to 99, display "ok" and break the loop.
"""
for key in list.keys():
  if key >= 99:
    print("ok")
    break

"""
Loop through a dictionary's keys. Add each item—both its key and value—to a second dictionary. Make everything up.
"""

newlist = {}
for key in list.keys():
  newlist[key] = list[key]

"""
Loop through the dictionary's keys, displaying each of the dictionary's values. Store the keys in the variable a_key.
"""
hardness_scale = {
    "talc": 1,
    "gypsum": 3,
    "calcite": 9,
}
for a_key in hardness_scale.keys():
    print(hardness_scale[a_key])
"""
Loop through the hardness_scale dictionary, adding each key-value pair in it to the minerals dictionary. Display the minerals dictionary.
"""
minerals = {}
hardness_scale = {
    "talc": 1,
    "gypsum": 3,
    "calcite": 9,
}

for key in hardness_scale.keys():
  minerals[key] = hardness_scale[key]
print(minerals)
