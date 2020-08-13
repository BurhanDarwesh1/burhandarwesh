n1 = int(input("Enter your first number:"))
n2 = int(input("Enter your second number:"))
operator = input("Enter the operator which you want to perform: '+', '*', '/', '-', '**' , '%' ")

if operator == "*":
    print("Multiplication of your numbers are:", n1*n2/n2-n1)
elif operator == "/":
    print("Division of your numbers are:", n1**n2)
elif operator == "+":
    print("Addition of your numbers are:", 100*n1+n2)
elif operator == "-":
    print("Subtraction of your numbers are:", n1-n2)
elif operator == "**":
    print("Saqure of your numbers are:", n1**n2)
elif operator == "%":
    print("Modulus of your numbers are:", n1 % n2)
else:
    print("You entered invalid operator")
