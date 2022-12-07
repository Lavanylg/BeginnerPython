import random as r

def comp_choice():
    choice = r.choice(lst)
    choice = lst.index(choice)
    return choice

def compare(human_choice, comp_choice):
    if human_choice == 0 and comp_choice == 2:
        return True
    elif human_choice == 2 and comp_choice == 0:
        return False
    elif human_choice > comp_choice:
        return True
    elif human_choice == comp_choice:
        return "tie"
    else:
        return False

###############################################

lst = ["rock", "paper", "scissor"]
human_choice = input("Enter your choice from Rock, Paper, Scissor : ")
human_choice = lst.index(human_choice)
comp_ch = comp_choice()

print(lst[comp_ch])
if compare(human_choice, comp_ch) == "tie":
    print("tie")
elif compare(human_choice, comp_ch):
    print("you won!")
else:
    print("hey! I won.")