# 5. Write a program which finds out whether a given name is present in a list or not.
names = ["Harry","Arjun","Mohan","divya","Krish"]
inpName = (input("Enter the name: "))
if(inpName in names):
    print("The given name is present in the list!")
else:
    print("The given name is not present in the list!")