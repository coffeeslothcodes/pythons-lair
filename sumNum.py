limit = int(input("Enter the limit: "))
current_sum = 0

for i in range(1, limit + 1):
    current_sum += i
    
print(f"The sum of natural numbers up to {limit} is: {current_sum}")