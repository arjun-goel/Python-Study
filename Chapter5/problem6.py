# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.

l = {}  # created a dictionary

name1 = input("Enter your name:  ")
language1 = input("Enter your language:  ")
l.update({name1: language1})

name2 = input("Enter your name:  ")
language2 = input("Enter your language:  ")
l.update({name2: language2})

name3 = input("Enter your name:  ")
language3 = input("Enter your language:  ")
l.update({name3: language3})

name4 = input("Enter your name:  ")
language4 = input("Enter your language:  ")
l.update({name4: language4})

print(l)