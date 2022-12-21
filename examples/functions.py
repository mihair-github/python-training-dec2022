def print_greeting():
    """Prints 'hello world'"""
    print("hello world")


print_greeting()
value_returned = print_greeting()
print("Value returned by print_greeting:", value_returned)


def get_greeting():
    """Returns 'hello world'"""
    return "hello world"


greeting = get_greeting()
print("Value returned by get_greeting:", greeting)


def greet(name):
    print(f"Hello, {name}!")


greet("Ana")
greet("Andrei")


def decrement(nr, step=1):
    return nr - step


print(decrement(10))
print(decrement(10, 2))
print(decrement(step=3, nr=10))


def varargs(*args, **kwargs):
    print(args, type(args), len(args))
    # for arg in args:
    #     print(arg)
    print(kwargs, type(kwargs), len(kwargs))
    # for k, v in kwargs.items():
    #     print(k, v)
    # name = kwargs.get("name")
    print()


varargs()
varargs(10)
varargs(10, 20)
varargs(10, 20, 10, 40, 50)

varargs(name="Ana", age=20, height=1.7)
varargs("hello", "world", 10, 15, name="Ana", age=20)