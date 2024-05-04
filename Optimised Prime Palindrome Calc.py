import time
import random


def miller_rabin_is_prime(n, k=40):
    if n <= 3:
        return n >= 2
    if n % 2 == 0:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for _ in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not check(a, s, d, n):
            return False
    return True


def generate_palindromes_in_range(minimum, maximum):
    start_time = time.time()
    primes = []
    # For even-length palindromes
    for i in range(minimum, maximum):
        s = str(i)
        palindrome = int(s + s[-1::-1])
        if palindrome >= maximum:
            break
        if palindrome >= minimum and miller_rabin_is_prime(palindrome):
            primes.append(palindrome)

    # For odd-length palindromes
    for i in range(minimum, maximum):
        s = str(i)
        palindrome = int(s + s[-2::-1])
        if palindrome >= maximum:
            break
        if palindrome >= minimum and miller_rabin_is_prime(palindrome):
            primes.append(palindrome)

    end_time = time.time()
    print(f"Took {end_time - start_time} seconds")
    print("There are", len(primes), "special numbers in the specified range.")

    if len(primes) >= 6:
        print("First 3 smallest prime palindromes:")
        for prime_palindrome in sorted(primes)[:3]:
            print(prime_palindrome)

        print("\nLast 3 largest prime palindromes:")
        for prime_palindrome in sorted(primes)[-3:]:
            print(prime_palindrome)
    else:
        print("Prime palindromes:")
        print(primes)


minimum = int(input("Enter the minimum value: "))
maximum = int(input("Enter the maximum value: "))
generate_palindromes_in_range(minimum, maximum)



