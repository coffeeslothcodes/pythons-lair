num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial for numbers below zero do not exist.")
elif num == 0:
    print("Factorial of {num} is 1.")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print(f"The factorial of {num} is {factorial}.")