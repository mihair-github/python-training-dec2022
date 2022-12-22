import functools


def make_pretty(func):  # func is a local variable for make_pretty
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("I got decorated")  # added behaviour
        # print('args', args, type(args), func)
        # func is a variable from outer (enclosing) scope
        return func(*args, **kwargs)

    return inner  # inner will replace func


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
