"""
The dictionary name is products. Add an item to it. The key is "laptop".
The value is 397.50.
"""
products = {"laptop" : 400}
products["laptop"] = 397.50
print(products)

# Add a string element to a list, using the plus sign. Make up the string and the list name.
list = []
list = list + ["new item"]

# Add two elements to a list using the plus sign. The elements are numbers. Make everything up.
list = list + [2, 4]

# Add two items to a dictionary. All keys and values are strings. Make everything up.
dc = {}
dc["1"] = "a"
dc["2"] = "b"
# Add a string to the end of a list using the append keyword. Make up the list name and the string.
list.append(3)
print(list)


# Add an item to the dictionary. The key is "gold". The value is 1281.
# Targeting the gold item in the dictionary, display gold's price.

prices = {
  "ethanol": 1.531,
  "natural gas": 2.892,
  "gasoline": 1.5646,
}
prices["gold"] = 1281

print(prices['gold'])


# Code a dictionary with three items. Then add a fourth item to the dictionary.
# Display the complete dictionary.
prices = {
  "ethanol": 1.531,
  "natural gas": 2.892,
  "gasoline": 1.5646,
}
prices["gold"] = 1281
print(prices)