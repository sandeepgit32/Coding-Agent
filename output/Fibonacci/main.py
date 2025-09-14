def generate_fibonacci_series(n_terms):
    """
    Generate the Fibonacci series up to n_terms elements.

    Args:
        n_terms (int): The number of terms to generate. Must be a positive integer.

    Returns:
        list: The Fibonacci series as a list of integers.

    Raises:
        ValueError: If n_terms is not a positive integer.
    """
    if not isinstance(n_terms, int):
        raise ValueError("Number of terms must be an integer.")
    if n_terms <= 0:
        raise ValueError("Number of terms must be a positive integer (n_terms > 0).")

    series = []
    a, b = 0, 1
    for _ in range(n_terms):
        series.append(a)
        a, b = b, a + b
    return series

def main():
    """
    Entry point for Fibonacci series generation. Prints the Fibonacci series.
    """
    try:
        n = 10  # You may replace this with any desired number of terms
        result = generate_fibonacci_series(n)
        print(f"Fibonacci series with {n} terms: {result}")
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()

# Execution Output:
# Fibonacci series with 10 terms: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]