import random
number = random.randint(1,9)
count = 0
guess = 0

while guess != number and guess != "exit":
    guess = input("num between 0 to 10")
    if guess == "exit":
        break
    guess = int(guess)
    count += 1
    if guess < number:
        print("its low")
    elif guess > number:
        print("its high")
    else:
        print("you got it")
        print("you took",count,"tries to get it right")




        

