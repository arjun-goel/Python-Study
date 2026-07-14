# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
name = (input("Enter the name: "))
date = (input("Enter the date: "))
# Using of f will help u implement the input from other variables , it is the new feature of python

letter = f'''         
Dear {name},
You are selected!
{date}
'''
print(letter)