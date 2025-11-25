import random
print("Welcome! In the game of guessing word!!!")
List=["basma","nasma","ahmed","Hamsa"]
chance=0
ch=5
gu=(random.choice(List))
while chance<ch:
    chance+=1
    guess=input("Guess word: ")
   
       
    if guess==gu:
            print("Correct ! You guessed the correct word ")
            break
    elif guess!=gu:
            print("Sorry! Try again ")
            

else:
    print("You finished your chance ,Good luck in the next time")
    

