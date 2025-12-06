def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
    Non-negative integer

    Returns:
    Factorial of n
    """

    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
        return result

n = int(input("Enter Number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:    
    print("Factorial After Calculate =",calculate_factorial(n))