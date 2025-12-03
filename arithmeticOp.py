#addition
print("Addition")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addresult= num1+num2
print(f"Addition: {num1} + {num2} = {addresult}")

#subraction
print("Subtraction")
num3 = float(input("Enter the first number: "))
num4 = float(input("Enter the second number: "))
subresult= num3-num4
print(f"Subtraction: {num3} - {num4} = {subresult}")

#multiplication
print("Multiplication")
num5 = float(input("Enter the first number: "))
num6 = float(input("Enter the second number: "))
mulresult=num5*num6
print(f"Multiplication: {num5} * {num6} = {mulresult}")


#division
print("Division")
num7 = float(input("Enter the first number: "))
num8 = float(input("Enter the first number: "))
if num8 == 0:
    print("Math Error: Cannot divide by zero.")
else:
    divresult= num7/num8
    print(f"Division: {num7} / {num8} = {divresult}")
