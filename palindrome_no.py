def is_palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return temp == rev

print(is_palindrome(1231))  # Output: True