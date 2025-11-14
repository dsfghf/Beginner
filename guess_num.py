import random
print("Welcome in guessing game! \n You have 5 chances to guess the correct number! ")
low=int(input("Enter the lower number: "))
high=int(input("Enter the upper number: "))
ch=5
chance=0
num=random.randint(low,high)
while chance<ch:
    chance+=1
    guess=int(input("Enter your guess:: "))
    if guess==num:
        print(f"Correct! You guessed the correct number{num} ")
        break
    elif guess !=num :
        print("Sorry! Try again")
    elif guess< num:
        print("This i very low ! Try again ")
    elif guess >num:
        print("This is very high !! Try again ")
else:
    print("Good luck in the next time !")
