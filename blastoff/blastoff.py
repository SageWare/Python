##################
# blastoff
# Sage Fremont
##################

# Get user input as a string
userInput = (int)(input("Please enter an integer: "))


def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)


def countdown(o):
    if o <= 0:
        print('Blastoff!')
    else:
        print(o)
        countdown(o-1)

if userInput >= 0:
    countdown(userInput)
if userInput <= 0:
    countup(userInput)
