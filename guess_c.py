import random
name=input("Whats your name? ")
print(f"Welcome {name} in Guessing game !!! ")
words=['hello','Hello','Hi','banan','apple','mango']
word=random.choice(words)
print("Guess the characters ")
guesses=''
turns=14
while turns>0:
       
        failed=0
        for char in word:
           if char in guesses:
             print(char,end=" ")
           else:
             print("_")
             failed+=1
        if failed==0:
            print(" \nYOU win ")
            print(f"The word is :: {word}")
            break
        print()
        guess=input("guess a character:: ")
        guesses+=guess
        if guess not in word:
            turns-=1
            print("Wrong")
            print(f"You have {turns},more guesses ")
            if turns==0:
                print("You loose")