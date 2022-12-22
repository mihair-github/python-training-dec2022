from decorators import print_exec_time


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


def return_html(tag: str, content: str):  # type hints
    escape_chars = {
        ord('<'): '&lt;',
        ord('>'): '&gt;',
        ord('"'): '&quot;',
        ord('&'): '&amp;'
    }
    content = content.translate(escape_chars)

    return f'<{tag}>{content}</{tag}>'


print(return_html("b", "Ham & Eggs"))


@print_exec_time
def long_fun(n):
    cn = 0
    for i in range(n):
        cn = cn + i
    return cn


print(long_fun(100000))
print(long_fun(100000))
print(long_fun(100000))
print(long_fun(100000))
print(long_fun(100000))
print(long_fun(100000))
