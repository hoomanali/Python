# Ali Hooman
# alhooman@ucsc.edu
#
# Programming Assignment 8
# Multiply numbers: a * b

print("------Mult------")

a = int(input("Enter non-negative first number: "))
while a < 0:
    a = int(input("Enter non-negative first number: "))

b = int(input("Enter non-negative second number: "))
while b < 0:
    b = int(input("Enter non-negative second number: "))

# Increments a number
def inc(n: int) -> int:
    return n + 1

# Decrements a number
def dec(n: int) -> int:
    return n - 1

# Sums two numbers
def add(n: int, m: int) -> int:
    if m == 0:
        return n
    else:
        return add(inc(n), dec(m))

# Multiplies two numbers
def mul(n: int, m: int) -> int:
    if m == 0 or n == 0:
        return 0
    else:
        return add(n, mul(n, dec(m)))

result = mul(a,b)
print(a, "x", b, "=", result)
