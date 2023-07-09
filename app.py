print("Welcome to Python") #this is a comment

#this function is for adding 2 numbers
def add_num (x, y):
    print("the total is", x+y)

#these are the user inputs who ask the user for numbers to add
ask_user = int(input("choose a number"))
ask_user2 = int(input("choose another number"))

#this is the function call
add_num(ask_user, ask_user2)

print("This is the first print with the new branch")