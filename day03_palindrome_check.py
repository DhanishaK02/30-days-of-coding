# Day 03: Palindrome Check

def is_palindrome(s):
    return s == s[::-1]

text = "madam"

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")
