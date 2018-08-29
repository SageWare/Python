#compare_bool.py
#author Sage Fremont
#Program that compares two numbers entered by the user


#Function for first number
def getFirstNumber():
    a = int(input("Enter your first number "))
    return a

#Prompt & Store first number as variable a
a = getFirstNumber()

#Function for second number
def getSecondNumber():
    b = int(input("Enter your second number "))
    return b

#Prompt & store second number as variable b
b = getSecondNumber()

#The Compare Function
def compare(a, b):
    if a > b:
        return 1
    if a == b:
        return 0
    if a < b:
        return -1

#a blank line for clean output spacing
print("")

#Compare a and b
print("The comparison of your numbers return:")
print(compare(a, b))

#a blank line for clean output spacing
print("")

#Testing set values for debugging
print("The following is a test of set values:")
print(compare(5,2))
print(compare(2,5))
print(compare(3,3))
