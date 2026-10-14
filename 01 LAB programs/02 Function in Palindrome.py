# 7. Write a function that takes a string input and checks if it‘s a palindrome or not. 


def is_palindrome(text):
    text_str = str(text)
    reverse_text = text_str[::-1]

    if text_str == reverse_text:
        return True
    else:
        return False

## ex1:
p = is_palindrome(1232)
print(p)

## Ex2:
pn = is_palindrome("AAABBBAAABBBAAA")
print(pn)























