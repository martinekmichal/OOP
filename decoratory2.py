def my_decorater(my_function):
    print("prvy print")
    def simple_wrapper(arg1, arg2):
        print("druhy print")
        result = my_function(arg1, arg2)
        print("treti print")
        return result
    return simple_wrapper


def add(a, b):
    return a + b


new_function = my_decorater(add)
result = new_function(4, 5)

print(result)

result2 = my_decorater(add)(11, 12)
print(result2)


@my_decorater
def minus(a, b):
    return a - b

r3 = minus(100, 30)
print(r3)