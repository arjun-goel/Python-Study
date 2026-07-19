# 6. Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter the number: "))
check = 0

if(num==0):
    print(1)
    check = 0
elif(num<0):
    print("The Number should be positive!") 
    check = 0   
else:
    for i in range(num-1,0,-1):
        num = num*i
    check = 1
        
if(check==0):
    pass
elif(check==1):
    print(num)