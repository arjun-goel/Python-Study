# 5. Write a program to find the sum of first n natural numbers using while loop.
num = int(input("Enter the number: "))
i = 1
add = 0
while(i<num+1):
    add = add + i
    i+=1
print(add)    