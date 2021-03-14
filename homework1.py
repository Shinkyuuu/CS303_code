# Cody Park / CS 303

def gcd():  # Euclidean Algorithm
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))
  if a > b:  # If 'a' > 'b', swap them.
    a, b = b, a

  r = a % b  # Find the remainder 'r' between 'a' and 'b'

  while r > 0:  # While (r > 0), replace 'a' with 'b' and 'b' with 'r'. Then divide and find a new remainder.
    a, b = b, r
    r = a % b

  print("gcd is " + str(b))
  return b  # Return the greatest common divisor


gcd()