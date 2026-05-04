# Print prime numbers from 1 to 100

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [str(i) for i in range(1, 101) if is_prime(i)]
print("Primes from 1 to 100:")
print(", ".join(primes))
