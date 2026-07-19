# 1. Add Two Numbers
def add(a, b):
    return a + b
print("1.", add(10, 20))

# 2. Square of a Number
def square(n):
    return n * n
print("2.", square(6))

# 3. Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    return b
print("3.", largest(15, 25))

# 4. Check Even or Odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"
print("4.", even_odd(9))

# 5. Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print("5.", factorial(5))

# 6. Check Prime Number
def prime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
print("6.", prime(13))

# 7. Reverse a String
def reverse_string(s):
    return s[::-1]
print("7.", reverse_string("Python"))

# 8. Count Vowels
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count
print("8.", count_vowels("Hello World"))

# 9. Sum of List
def list_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total
print("9.", list_sum([10, 20, 30, 40]))

# 10. Check Palindrome
def palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    return "Not Palindrome"
print("10.", palindrome("madam"))