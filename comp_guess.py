import random

MINIMUM = 0
MAXIMUM = 100
NUMBER = random.randint(MINIMUM, MAXIMUM)
TRY = 0
RUNNING = True
ANSWER = None

while RUNNING:
    print ("Is it %s?" % str(NUMBER))
    ANSWER = input("")
    if ANSWER.lower() == "no":
        print("Higher or Lower")
        ANSWER = input("")
        if ANSWER.lower() == "higher":
           NUMBER += random.randint(1, 4)
        elif ANSWER.lower() == "lower":
           NUMBER -= random.randint(1, 4)
    elif ANSWER.lower() == "yes":
            print("comp took %s tries to guess" % str(TRY))
            RUNNING = False
         
    TRY +=1

print("Thanks for game")     

