#compare_bool.py
#author Sage Fremont
#Program that compares two numbers entered by the user


#Prompt user to enter first number
def getFirstNumber():
    a = int(input("Enter your first number "))
    return a

#Storing first number input as variable a
a = getFirstNumber()

#Prompt user to enter second number
def getSecondNumber():
    b = int(input("Enter your second number "))
    return b

#Storing second number input as variable b
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

#Printing the return of The Compare Function's a & b values via user input
print("The comparison of your numbers return:")
print(compare(a, b))

#a blank line for clean output spacing
print("")

#Testing Set Values
print("The following is a test of set values:")
print(compare(5,2))
print(compare(2,5))
print(compare(3,3))
