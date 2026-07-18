# 2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.

English_Marks = int(input("Enter the marks in english: "))
Maths_Marks = int(input("Enter the marks in maths: "))
Physics_Marks = int(input("Enter the physics: "))

total_marks = English_Marks+Maths_Marks+Physics_Marks

if((English_Marks<33 or Maths_Marks<33 or Physics_Marks<33) or (total_marks/3)<40):
    result = 0
else:
    result = 1


if(result==0):
    print("Failed!")
else:
    print("Passed!") 