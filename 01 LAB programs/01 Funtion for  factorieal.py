## 6. Write a function that takes an integer input and calculates the factorial of that number.

def calculate_factorial(num):
    factorial = 1
    while num > 0:
        factorial = factorial * num
        num = num - 1
    return factorial

user_input  = input("Enter a any number: ")
numbers = int(user_input)

result = calculate_factorial(numbers)
print(result)

