 #Python weight converter 

weight = float(input("Enter your weight: "))
unit = input(" kilograms or pounds? (K or P):")

if unit == "K":
   weight = weight * 2.205
   unit = "LBS"
elif unit == "P":
   weight = weight / 2.205
   unit = "KGS"
else:
    print(f"{unit} is not a valid unit. Please enter K or P.")

print(f"Your weight is {weight}{unit}")

