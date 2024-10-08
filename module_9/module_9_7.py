# Задача по теме "Декораторы".

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        return result
    return wrapper
    # return func


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
