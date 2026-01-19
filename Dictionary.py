# a dictionary is a built-in data type that stores data in key-value pairs.
# It is an unordered, mutable, and indexed collection. Each key in a dictionary is unique and maps to a value
# no key without value
sports_player = {
   "Name": "Sachin Tendulkar",
   "Age": 48,
   "Sport": "Cricket"
}
print ("Dictionary using curly braces:", sports_player)
# Creating a dictionary using the dict() function
student_info = dict(name="Alice", age=21, major="Computer Science")
print("Dictionary using dict():",student_info)  


# Only a number, string or tuple can be used as key. All of them are immutable. You can use an object of any type as the value.
# Python doesn't accept mutable objects such as list as key, and raises TypeError.


d1 = {"Fruit":['Mango',"Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):{'coun':'iwo'}, ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)


# You can assign a value to more than one keys in a dictionary, but a key cannot appear more than once in a dictionary.
d1 = {"Banana":"Fruit", "Rose":"Flower", "Lotus":"Flower", "Mango":"Fruit"}
d2 = {"Fruit":"Banana","Flower":"Rose", "Fruit":"Mango", "Flower":"Lotus"}
print (d1)
print (d2)

# You can access the value associated with a specific key using square brackets [] or the get() method

student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
# Accessing values using square brackets
name = student_info["name"]
print("Name:",name)  

# Accessing values using the get() method
age = student_info.get("age")
print("Age:",student_info.get("age"))  

# Modifying an existing key-value pair
student_info["age"] = 22

# Adding a new key-value pair
student_info["graduation_year"] = 2023
print("The modified dictionary is:",student_info)

# Removing an item using the del statement
del student_info["major"]

# Removing an item using the pop() method
student_info.pop("graduation_year")

print(student_info) 

# Iterating through keys
for key in student_info:
   print("Keys:",key, student_info[key])

# Iterating through values
for value in student_info.values():
   print("Values:",value)

# Iterating through key-value pairs
for key, value in student_info.items():
   print("Key:Value:",key, value) 