"""
Loop through a dictionary, getting both keys and values. Display the values. Make everything up.
"""
list = {0: '1', 4: '5'}
for key, value in list.items():
  print(value)

"""
Loop through a dictionary, getting both keys and values. 
Display "The key is " and then the key. Remember to include a space at the end of the string. 
Make everything up.
"""
for key, value in list.items():
  print('The key is', key)

"""
Loop through a dictionary, getting both keys and values. If you find an item that has the same key and value, 
display "weird" and break the loop. Make up the names of everything.
"""
for key, value in list.items():
  if key == value:
    print("weird")
    break

