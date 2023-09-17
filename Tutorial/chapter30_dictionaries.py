# Eliminate a list element using the element's value, which is "gold". Make up the name of the list.
list = ["silver","gold"]
list.remove("gold")

# remove element using index
del list[0]

# delete second number
numbers = {
  "first": 1,
  "second": 2,
  "third": 3,
  "fourth": 4,
}

del numbers["second"]

#Change the value of the third item to 3.0
numbers = {
  "first": 1,
  "second": 2,
  "third": 3,
  "fourth": 4,
}
numbers["third"] = 3.0
# Code a three-item dictionary in five lines of code. Then delete the first item.
# The keys are numbers. The values are strings. Make everything up.
list = {
0: '1',
1: '2',
2: '3'
}

del list[0]
print(list)