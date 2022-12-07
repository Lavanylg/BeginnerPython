import random as r

def gen_pwd(amt, length):
    for i in range(amt):
        for j in range(length):
            print(chr(r.randint(2,100)), end='')
        print()

##########################################################

amt = int(input("Enter the number of passwords : "))
length = int(input("Enter the length of the password : "))

gen_pwd(amt, length)
