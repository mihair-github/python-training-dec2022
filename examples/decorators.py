import functools
import time


def make_pretty(func):  # func is a local variable for make_pretty
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("I got decorated")  # added behaviour
        # print('args', args, type(args), func)
        # func is a variable from outer (enclosing) scope
        return func(*args, **kwargs)

    return inner  # inner will replace func


def doubler(func):  # func is a local variable for make_pretty
    @functools.wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return inner  # inner will replace func


@make_pretty
@doubler
def get_sum(a, b, c):
    return a + b + c
# get_sum = make_pretty(doubler(get_sum))
# get_sum = make_pretty(doubler(params)(get_sum))


def print_exec_time(func):
    def inner(*args, **kvargs):
        t1 = time.time()
        inner_result = func(*args, **kvargs)
        t2 = time.time()
        print(f'Function run for: {t2 - t1} s')
        return inner_result
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


@make_pretty
def greet(name):
    print(f"Hello, {name}!")


@make_pretty
def decrement(nr, step=1):
    """Decrements nr with step"""
    return nr - step


# ordinary = make_pretty(ordinary)  # decoration
# pretty == make_pretty.<locals>.inner

ordinary()  # make_pretty.<locals>.inner()
print()

greet("Ana")  # make_pretty.<locals>.inner("Ana")
print()

decremented_val = decrement(9)  # make_pretty.<locals>.inner(9)
print("Decremented value:", decremented_val, end="\n\n")

decremented_val = decrement(9, step=3)  # make_pretty.<locals>.inner(9, step=3)
print("Decremented value:", decremented_val, end="\n\n")

print(f"Decrement function's name is <{decrement.__name__}> and does "
      f"<{decrement.__doc__}>.")


print("Sum is", get_sum(1, 2, 3))