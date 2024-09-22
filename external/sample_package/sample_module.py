def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Args:
    n (int): A non-negative integer

    Returns:
    int: The factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
