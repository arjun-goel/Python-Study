marks = int(input("Enter your marks: "))
if(marks <= 100 and marks > 90):
    grade = 1
elif(marks <= 90 and marks > 80):
    grade = 2
elif(marks <= 80 and marks > 70):
    grade = 3
elif(marks <= 70 and marks > 60):
    grade = 4
elif(marks <= 60 and marks > 50):
    grade = 5
elif(marks<50):
    grade = 6
else:
    grade = 7
    

if(grade==1):
    print("Excellent!")
elif(grade==2):
    print("A")
elif(grade==3):
    print("B")
elif(grade==4):
    print("C")
elif(grade==5):
    print("D")
elif(grade==6):
    print("F(failed!)")
else:
    print("You have given incorrect input, the maximum range is till 100")    
   