# Write a program to print the following pattern:-
# n = 3
# * * *
# * * 
# * * *
# Logic Building Step:-
# r1 = 3 stars
# r2 = 2 stars           
# r3 = 3 stars

n = 3
stars = 3
for i in range(1,n+1):
    for j in range(stars):
        print("*",end="")
    print()
    if(stars == 3):
        stars = 2
    else:
        stars = 3