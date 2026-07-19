# 4. Write a program to find whether a given number is prime or not.
# check = 0 means num is not prime
# check = 1 means num is prime
num = int(input("Enter the number: "))

if(num<=1):
    check = 0
    
elif(num==2):
    check = 1

for i in range(2,num):
    if(num%i==0):
        check=0
        break
    else:
        check=1

if(check==0):
    print("The number is not prime")
elif(check==1):   # I can also use else: in place of elif(check==1):
    print("The number is prime")