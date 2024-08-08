# В алгоритме применено Решето Эратосфена

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
is_prime = [True] * len(numbers)

for i in range(2, len(numbers)):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, len(numbers), i):
            is_prime[j] = False
    else:
        not_primes.append(i)

print(primes)
print(not_primes)