# A recursive program to generate N terms
def fibonacci_term(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_term(n - 1) + fibonacci_term(n - 2)

def generate_fibonacci(n):
    if n <= 0:
        return []
    return [fibonacci_term(i) for i in range(1, n + 1)]

n = int(input("Enter number of terms N: "))
print(f"First {n} Fibonacci terms:", generate_fibonacci(n))