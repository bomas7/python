#Quick unoptimized prime factorization

primes = []

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_factorization(n):
    factors = [i for i in range(2, n+1) if n % i == 0]
    largest = max([i for i in factors if is_prime(i)])
    other = int(n/largest)
    if is_prime(other):
        primes.append(largest)
        primes.append(other)
        return
    primes.append(largest)
    prime_factorization(other)
    

def main():
    n = int(input('n: '))
    if is_prime(n):
        print('The number is prime')
        return
    else:
        prime_factorization(n)
        print(sorted(primes))

if __name__ == '__main__':
    main()
