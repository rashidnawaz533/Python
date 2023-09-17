# The dictionary has just one item. The dictionary's
# name is x. The key is "A12". The value is 9.99 Code the dictionary.
x = {"A12": 9.99}
'''
Code a two-item dictionary, breaking the code into four lines.
All keys and values are strings. Don't forget to indent properly. Don't forget the optional 
comma after the second item. Make everything up.
'''

new_dictionary = {
    "first_name": "Rashid",
    "last name": "Nawaz",
    "age": "16",
    "work": "code"
}
print(new_dictionary['first name'])

'''
Code a three-item dictionary on five lines. The keys are integers. The values are floats. 
Display the sum of the dictionary's three values.
'''
new_dictionary = {
    0 : 0.1,
    1: 0.2,
    2: 0.3
}
sum = 0
for val in new_dictionary.values():
  sum += val
print(sum)

