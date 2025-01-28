# python compound interest calculator

print("Welcome to the compound interest calculator")
print("Please enter the following details to calculate the compound interest")

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

# formula to calculate compound interest
compound_interest = principal * (pow((1 + rate / 100), time))

print("Compound interest is: ", compound_interest)

# Output