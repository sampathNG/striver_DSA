# PRINT NUJBERS TABLE IN REVEWRSE ORDER USING WHILE LOOP #
# x = int(input("Enter a number: "))
# y=10
# while y > 0:
#     print(x*y)
#     if y == 0:
#         break
#     y-=1
# ************************************************************************
# find n-th term of Fibonacci series 
n = int(input("Enter a number : "))
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for i in range(3, n + 1):
        c = a + b
        a, b = b, c
    return b
print(f"The {n}-th Fibonacci term is: {fibonacci(n)}")
