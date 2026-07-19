# 10. Write a program to print multiplication table of n using for loops in reversed order.
n = int(input("Enter the value of n: "))
for i in range(n*10,n-1,-n):
    print(i)