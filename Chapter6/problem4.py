# 4. Write a program to find whether a given username contains less than 10 characters or not.
username = (input("Enter the username: "))
length = len(username)
if(length<10):
    print("Username is less than 10 characters!")

else:
    print("Username is NOT less than 10 characters!")