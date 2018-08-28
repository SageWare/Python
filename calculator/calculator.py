###############################################################
# Calculator
# author Sage Fremont
###############################################################


while True:
    #Prompt User to enter first number > 0
    num1 = int(input('Please enter a whole number greater than 0 and press ENTER.\n'))
    while num1 <= 0:   
        print('The number must be greater than 0.\n')
        num1 = int(input('Please enter a whole number greater than 0 and press ENTER.\n'))

    #Prompt User to enter second number > 0
    num2 = int(input('Please enter another whole number greater than 0 and press ENTER.\n'))
    while num2 <= 0:                                                  
        print('The number must be greater than 0.\n')
        num2 = int(input('Please enter another whole number greater than 0 and press ENTER.\n'))

    #Prompt User to enter an operator & print calculation
    oper = input('Please enter an operator such as; +, -, *, or / and press ENTER.\n')
    if oper != "+" and oper != "-" and oper != "*" and oper != "/":
        print ("You entered an invalid operator.")
        oper = input('Please enter an operator such as; +, -, *, or / and press ENTER.\n')
    if oper == "+":
        print (num1,'+',num2,'=',num1 + num2)
    if oper == "-":
        print (num1,'-',num2,'=',num1 - num2)
    if oper == "*":
        print (num1,'*',num2,'=',num1 * num2)
    if oper == "/":
        print (num1,'/',num2,'=',num1 / num2)

    #Option to perform another calculation
    response = input("Would you like to perform another calculation? (y/n)\n")
    if response != "y":
        print("Goodbye.")
        break


