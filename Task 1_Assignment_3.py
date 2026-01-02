
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Taking input from the user
num = int(input("Enter a number: "))

# Calling the function
result = factorial(num)

# Printing the output
print(f"Factorial of {num} is : {result}")

