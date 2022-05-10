first_number = float(input("Enter a number: "))
operator = input("Enter an operator (addition(+),subtraction(-),division(/),multiplication(x): ")
second_number = float(input("Enter another number: "))

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "/":
    print(first_number / second_number)
elif operator == 'x':
    print(first_number * second_number)
else:
    print("Invalid Operator")
