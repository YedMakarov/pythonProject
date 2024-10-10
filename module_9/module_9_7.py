# Задача по теме "Декораторы".

def is_prime(func):
    def wrapper(*args):
        result = func(*args)

        if result <= 1:
            return f"Ни простое ни составное \n{result}"
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                return f"Составное \n{result}"
        return f"Простое \n{result}"

    return wrapper


@is_prime
def sum_three(*args: int):
    result = 0

    for i in args:
        result += i
    return result


# Main
result = sum_three(2, 3, 6)
print(result)

result = sum_three(2, 3, 7)
print(result)

result = sum_three(1, 0, 0)
print(result)
