"""
The length (number of dictionaries) of the customers list will be both the index number and the customer id of the new dictionary.
Code the line that finds the length of the customers list and assigns it to the variable new_customer_id.
"""
customers = [{},{},]
new_customer_id = len(customers)

"""
You've defined a new dictionary and assigned it to the variable new_dictionary. Now append it to the customers list.
"""
new_dictionary = {}
customers.append(new_dictionary)

"""
Find the number of elements in the list and assign the number to a variable. Then display the value of the variable.
"""
list_of_numbers = [1, 2, 3, 4, 5, 6]
length = len(list_of_numbers)
print(length)

"""
Using the variables new_customer_id, new_first_name and new_last_name, code a new dictionary.
Append the new dictionary to the list
Display the list.
"""
customers = [
  {
    "customer id": 0,
    "first name":"John",
    "last name": "Ogden",
  },
]
new_customer_id = len(customers)
new_first_name = "Ariel"
new_last_name = "Winter"

new_customer = {
  "customer id": new_customer_id,
  "first name": new_first_name,
  "last_name": new_last_name
}

customers.append(new_customer)
print(customers)