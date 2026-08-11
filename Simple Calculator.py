# A simple calculator scripted by Nihil using the if, elif and else statement. The script stops once you receive your answer.

# Welcome message
print("Hello user, thank you for using this simple calculator. \n Operators are listed below \n + to add \n - to subtract \n * to multiply \n / to divide \n % to return the remainder of a division (Modulus) \n ** for repeated multiplication (Exponentiation)")

# User inputs
a = float(input("Enter your first number > "))
b = input("Enter an operator > ")
c = float(input("Enter your second number > "))

if b == "+":
    result = a + c

elif b == "-":
    result = a - c

elif b == "*":
    result = a * c

elif b == "/":
    if c == 0:
        print("You can1t divide by zero.")
        result = None
    else:
        result = a / c

elif b == "%":
    result = a % c

elif b == "**":
    result = a ** c

else:
    print("Invalid Operator.")
    result = None

if result is not None:
    print("Your answer is", result)
