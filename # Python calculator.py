# Python calculator 

operator = input("enter an operator (+ - * /):")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2st number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
    
