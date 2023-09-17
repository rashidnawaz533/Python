# print every values in list using for loop
list = {'1','2','3'}
for val in list.values():
  print(val)

# Looping through the values in a dictionary, test if any of the values is less than 0.
# If so, display "ok" and break the loop.

list = {0:'1',1:'2',3:'3'}
for val in list.values():
    if val<0:
      print("ok")
      break

# Looping through the values in a dictionary, test if any of the values is equal to the modulo
# of 4 divided by 3. If so, display "ok" and break the loop.
list = {0:'1',1:'2',3:'3'}

for val in list.values():
    if 4%3 == val:
      print("ok")
      break


# Looping through the values in a dictionary, test if any of the values is equal to "arsenic".
# If so, append the value to the poisons list (use the variable from the loop, not the string,
# when appending) and break the loop.
poisons = []
list = {0:'1',1:'2',3:'3',4:'arsenic'}
for val in list.values():
    if 'arsenic' == val:
      poisons.append(val)
      break

# You loop through keys in a dictionary the same way you loop through values,
# but you substitute keys where you'd write values. Looping through the keys in a dictionary,
# test if any of the keys is equal to "curse". If so, delete that item and break the loop.

list = {0:'1',1:'2',3:'3','curse':'arsenic'}
for key in list.keys():
    if 'curse' == key:
      del list['curse']
      break

# Loop through the dictionary looking for "Amazon".
# If you find it, append the value to the list. (Use the variable, not the string, to append.)
# Break the loop.
# Display the list.

a_list = ["Argo", "Argon", "Altoona"]
sites = {
    "search": "Google",
    "social": "Facebook",
    "travel": "Travelocity",
    "retail": "Amazon",
}

for val in sites.values():
    if val == 'Amazon':
        a_list.append(val)
        break

print(a_list)