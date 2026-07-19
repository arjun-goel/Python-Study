# 7. Write a program to print the following star pattern.
# *       
# ***    
# ***** for n = 3

# concept => end = ""

n = 3

for i in range(1,n+1): #determines no. of rows
    for j in range(0,2*i - 1):#determines no. of stars
        print("*",end="")   
    print()