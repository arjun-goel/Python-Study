# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3
# Logic Building Step:-
#  rows and no of stars
# r1 = 1 star
# r2 = 2 star
# r3 = 3 star
n = 3
for i in range(1,n+1): #for determing the rows
    for j in range(0,i):  #for determing the no of stars in each row
        print("*",end="")
    print()