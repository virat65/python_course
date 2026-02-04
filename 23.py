

# print(add(5, 3))   # Output: 8


# arguments → input values

# expression → what the function returns (must be one line)
#  ✨ Example 1: Add two numbers

# add = lambda a, b: a + b

# print(add(5, 3))   # Output: 8


# ---

# ✨ Example 2: Square of a number

# square = lambda x: x * x

# print(square(6))   # Output: 36


# ---

# ✨ Example 3: Check even or odd

# even = lambda x: "Even" if x % 2 == 0 else "Odd"

# print(even(7))   # Output: Odd

# n= 5
# def fact():
#   # n = 6
#   print(n)
# fact()
# print(n)


# sum = lambda a,b:print(a+b)
# sum(12,222)
  # lambda arguments: expression
# add = lambda a, b: a + b
n = int(input("enter number "))
check = lambda n:"even" if n % 2 == 0   else "Odd"

print(check(n))


