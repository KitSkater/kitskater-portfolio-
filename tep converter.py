
unit = input("IS the temperature in Celsius or Fahrenheit?(C/F) ")
temp = float(input("What is the temperature? "))
if unit == "C":
    temp = temp * 9/5 + 32
    print(f"The temperature is {temp} degrees Fahrenheit.")
    pass
elif unit == "F":
    temp = (temp - 32) * 5/9
    pass
    print(f"The temperature is {temp} degrees Celsius.")
else:
    print("Invalid unit.")
    

