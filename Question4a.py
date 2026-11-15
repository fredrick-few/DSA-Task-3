# A recursive program to find the sum of first N natural numbers
def sum_natural(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

n = int(input("Enter N: "))
print(f"Sum of first {n} natural numbers: {sum_natural(n)}")