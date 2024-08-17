# "Пространство имен"

def test_function():
    pass

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


# Main
test_function()
inner_function()
