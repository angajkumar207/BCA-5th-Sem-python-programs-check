''' Funtion:
        - funtion in python reusable code into a block 
        - can be exicuted by calling the funtion name. 
        - this helps avoid repettion and make programs
        - modular and readable.'''
###     ther are many in built funtions in python like, print(), input(), len()

### funtion code:

# def hello(num1, num2):
#     reults = num1 + num2
#     return reults


# total = hello(4, 4)
# print(total)

##  Question no 1:
# 1.Write a function named welcome_user that takes a user's name 
# s a parameter and prints a personalized greeting like "Hello, [name]! Welcome."


# def welcome_user(name):
#     message = f"Hello {name}, welcome to my new Web application"
#     print(message)
#     return name
# welcome_user("Angaj")

##  Question no 2:
## 2. Square a Number: Create a function called square that takes one integer parameter, 
# calculates its square, and returns the result

# def square(num, n):
#     res = num ** n
   
#     return res

# total = square(5,2)
# print(total)


## 3. Area of a Rectangle: Write a function calculate_area that accepts length and width. 
# Give width a default value of 5. The function should return the total area.

# def find_area(length, width=5):
#     area = length * width
#     return area

# total_area = find_area(4)
# print(f"Area with default width (4*5)", total_area)

### 4. Even or Odd: Create a function called is_even that takes a number as 
# an argument and returns True if the number is even, and False if it is odd.

## method 1.
# def check_num(num):
#     if num % 2 == 0:
#         print("This num is Even", num)

#     else:
#         print("This number is odd", num)
# check_num(5)

## method 2.
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         False

# result = is_even(4)
# print(result)

#### 5. Find the Maximum: Write a function called find_max that takes three numbers as 
# arguments and returns the largest of the three without using Python's built-in max() function

# def find_largest_num(num1, num2, num3):
#     if num1 > num2:
#         print(num1)
#     if num2 > num3:
#         print(num2)
#     elif num3 > num1:
#         print(num3)

# find_largest_num(5, 6, 7)

## 6. Word Counter: Create a function named count_words that takes a single string 
# sentence as an input and returns the total number of words in that sentence.

# def count_word(word):
#     l = len(word)
#     return l

# s = count_word("Angaj")
# print(s)

## 7. Temperature Converter: Write a function celsius_to_fahrenheit that 
# converts a Celsius temperature to Fahrenheit using the formula (C * 9/5) + 32.

# def fahrenheit(c):
#     f = c * 9/5 + 32
#     return f

# s = fahrenheit(42)
# print(s)

## 8. List Filter: Write a function called filter_positive that takes a list of numbers (both positive and negative) 
# and returns a new list containing only the positive numbers.

# def Filter_positive(num_list):
#     possitve_list = []
#     for num in num_list:
#         if num > 0:
#             possitve_list.append(num)

#     return possitve_list
# mix_num = [5, -3,  7, 8, -9, 5]
# f = Filter_positive(mix_num)
# print(f)


### User Input
# def Filter_positive(num_list):
#     possitve_list = []
#     for num in num_list:
#         if num > 0:
#             possitve_list.append(num)

#     return possitve_list

# user_input = input("Enter num.....")
# num_list = [int(x) for x in user_input.split()]
# res = Filter_positive(num_list)
# print(res)

### 9. Palindrome Checker: Create a function is_palindrome that takes a string and returns True if the string reads 
# the same backward as forward (like "radar"), and False otherwise.

# def is_palindrome(text):
#     text_str = str(text)
#     reverse_text = text_str[::-1]
#     if text_str == reverse_text:
#         return True
#     else:
#         return False


# s = is_palindrome(12321)
# print(s)

## 10. The Multiplier: Write a function called multiply_all that uses *args to accept any number of numeric 
# arguments and returns the product of all of them multiplied together.

