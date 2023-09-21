"""
To check whether "weaving" is in the "electives" list inside the courses dictionary, complete the line.
"""
courses = {
    "electives":["weaving",],
}
if "weaving" in courses["electives"]:
    print()
"""
Test whether "red" is in the list within the dictionary.
specs = {
  "colors": ["green", "blue", "purple"],
}
"""
specs = {
  "colors": ["green", "blue", "purple"],
}

if "red" in specs["colors"]:
    print("ok")

"""
Test whether a color is in the list within the dictionary. If so, display "first". If not, 
test whether another color is in the list. If so, display "second". Your choice of colors.
specs = {
  "colors": ["green", "blue", "purple"],
}
"""
specs = {
  "colors": ["green", "blue", "purple"],
}
if "red" in specs["colors"]:
  print("first")
elif "blue" in specs["colors"]:
  print("second")

"""
Test whether a particular career is in the list. If so, display "yes". If not, display "no".
"""
details = {
  "nickname": "Flash",
  "married": "no",
  "careers": ["firefighter", "mathematician", "movie star"],
}
if "firefighter" in details["careers"]:
  print("yes")
else:
 print("no")

"""
If he is married and has "rock star" in his career list, display "Uh-oh". 
"""

details = {
  "nickname": "Mick",
  "married": "yes",
  "careers": ["firefighter", "mathematician", "rock star"],
}
if details["married"] == "yes" and "rock star" in details["careers"]:
  print("oh-oh")