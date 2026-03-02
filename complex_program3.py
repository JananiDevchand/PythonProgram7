def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    return False

# Example usage
if __name__ == '__main__':
    num = int(input("Enter a number to check if it's prime: "))
    print(f'{num} is prime: {is_prime(num)}')