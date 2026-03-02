def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage
if __name__ == '__main__':
    n = int(input("Enter the length of Fibonacci sequence: "))
    print(f'Fibonacci sequence of length {n}: {fibonacci(n)}')