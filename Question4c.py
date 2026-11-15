# A recursive program to find the Nth term of a Fibonacci series
def fibonacci_nth(n):
    if n <= 0:
        raise ValueError("N must be a positive integer.")
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_nth(n - 1) + fibonacci_nth(n - 2)

n = int(input("Enter term position N: "))
print(f"The {n}th Fibonacci term is: {fibonacci_nth(n)}")