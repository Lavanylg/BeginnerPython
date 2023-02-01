'''
Create Password:

Write a program that will:
● Display the intent of the program and list the password policy rules.
● Prompt the user to enter a password to be validated against the password policy.
● The program will enforce a password policy. The policy rules are as follows:
○ Have at least 2 uppercase A-Z letters.
○ Have at least 2 lowercase a-z letters.
○ Have at least 1 number.
○ Have at least 1 of the following special characters: @$!#%*?&
○ Have a minimum length of 8 characters.
● In addition to the password policy, the program will use a text file of commonly used passwords,
common_passwords.txt. The common_passwords.txt file will be located in the same directory as
the program.

○ For testing purposes, the team can create the common_passwords.txt file from the
example found below. However, the judges will use a different common_passwords.txt
file in scoring.

● The program will then check to see if the user-selected password is in the file.
● It will inform the user if their password does not follow the password policy and/or is too common.
○ If the password is not acceptable it will require them to enter a new password until all
criteria is met.

● Once the user has created a password that follows the password policy and is not found inside the
common_passwords.txt file, the program will inform the user that the password is acceptable to be
used.
● Prompt the user if they would like to validate another password or exit the program.
● Validate another password or exit based on the user’s input.
'''


print(" Create Password ".center(40,"*"))
print(" \tPassword Rules: \n Have at least 2 uppercase A-Z letters. \n Have at least 2 lowercase a-z letters. \n Have at least 1 number. \n Have at least 1 of the following special characters: @$!#%*?&. \n Have a minimum length of 8 characters.")
pw = input("Create your password : ")

chr_count = 0
num_count = 0
lower_count = 0
upper_count = 0
cap_alpha = "@$!#%*?&."
for i in range(len(pw)):
    if pw[i].isupper():
        upper_count += 1
    elif pw[i].islower():
        lower_count += 1    
    elif pw[i].isnumeric():
        num_count += 1         
    elif pw[i] in cap_alpha:
        chr_count += 1 
    else:
        print("Please create the password to follow the rules.")
        break

if len(pw) < 8:
    print("Please create password with >= 8 letters.")
if chr_count < 1:
    print("please check the password should have atleast one special characters.")
if num_count < 1:
    print("please check the password should have atleast one numbers.")
if lower_count < 2:
    print("please check the password should have atleast two lower letters.")
if upper_count < 2:
    print("please check the password should have atleast two upper letters.")

with open("password.txt", "r") as f:
    pwds = f.readlines()
    if pw + "\n" in pwds:
        print("Password already exists. Please choose another one.")