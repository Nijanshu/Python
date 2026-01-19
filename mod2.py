# mod2.py

import mod

fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
age= int(input("Enter your age: "))

name= mod.full(fname, lname)
age_months= mod.age_in_months(age)

print(f"Full name: {name} \n Age in months:{age_months}")