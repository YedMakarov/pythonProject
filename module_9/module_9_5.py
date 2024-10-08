# Задача "Range - это просто".

class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start: int, stop: int, step=1):
        self.start = start
        self.stop = stop
        if self.__no_zero_step(step):
            self.step = step
        self.pointer = self.start

    def __iter__(self):
        # Задать начальное значение указателя
        self.pointer = self.start
        return self

    def __next__(self):
        current = self.pointer

        # if self.step > 0:
        #     if current > self.stop:
        #         raise StopIteration()
        # else:
        #     self.step < 0
        #     if current < self.stop:
        #         raise StopIteration()

        if current > self.stop and self.step > 0 or current < self.stop and self.step < 0:
            raise StopIteration()
        else:
            self.pointer += self.step

        return current

    def __no_zero_step(self, step):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        else:
            return True


# Main

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
