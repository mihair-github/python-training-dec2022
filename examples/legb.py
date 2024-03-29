X = 100


def my_func(a):
    b = 1

    def inner(c):
        d = 3
        print("Built-in names (in inner's local scope):", len, int,
              ValueError)
        print("Global names (in inner's local scope):", X, my_func, MyClass)
        print("Enclosing names (in inner's local scope):", a, b, inner)
        print("Local names (in inner's local scope):", c, d, end="\n\n")

    inner(4)

    print("Built-in names (in my_func's local scope):", len, int, ValueError)
    print("Global names (in my_func's local scope):", X, my_func, MyClass)
    print("Local names (in my_func's local scope):", a, b, inner, end="\n\n")


class MyClass:
    pass


def func_using_imports_module():
    import imports  # local import
    print(imports.IMPORTS_VAR)


if __name__ == "__main__":  # if this module is run / sent as argument to python
    my_func(2)

    print("Built-in names (in global scope):", len, int, ValueError)
    print("Global names (in global scope):", X, my_func, MyClass)

    func_using_imports_module()
# else:  # if this module is imported
#     print(__name__, "was imported")
