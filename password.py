import sys

Master_Password = 'opensessame'
password = input("please enter the super secrete password: ")

attempt_count = 1

while password != Master_Password:
    password = input("invalid password. try again: ")
    attempt_count += 1
    
    if attempt_count > 3:
        sys.exit("Too many invalid password attempt.")
        
print("welcome to secrete town!")