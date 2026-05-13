'''Mail checking program:
users={"aareefashaik@gmail.com":"Aareefa",
       "pujithapalli3@gmail.com":"pallipuji"}
email=input("enter your mail id: ")
password=input("enter the pasword: ")
if email in users and users[email] == password:
    print("Login Successfully")
else:
    print("enter the correct pasword")

list_ = [12,67,5,3,7]
list2_ = [5,7,56]
new1 =[]
for i in list_:
    if i in list2_ :
        new1.append(i)
print(new1)'''
GAME IMPLEMENTING:
import random
score = 0
for round in range(1, 4):
    print("Round", round)
    computer = random.randint(1, 101)
    user = int(input("Guess a number between 1 to 100: "))             
    if user == computer:
        print("Correct Guess!")
        score += 2
    else:
        print("Wrong Guess!")
        print("Correct number was:", computer)
    print("Current Score:", score)
    print()
if score > 0:
    print("You Won")
else:
    print("You Fail")
