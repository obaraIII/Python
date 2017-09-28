import random
print("..............................................................................")
print("...............Guess the Number...............................................")
print("..............................................................................")
num = random.randint(0,10)
name = input("What is your name: ")

num1 = -1
while num1!=num:
    num1 = int(input("Hi, enter any number within the range of 0 and 10: "))
    #num1 = int(input("Hi ",name," pick a number between 0 & 100: "))
    if num1<num:
        print("Sorry", name, ", ", num1, " is too Low, Try again!: ")
    elif num1>num:
        print("Sorry", name, ", ", num1, " is too High, Try again!: ")
    elif num1 == num:
        print("Kudos, you got it right. Random number generated was ", num)
    else:
        print("Invalid Entry!!!")
print("..............Game Finished...................................................")
