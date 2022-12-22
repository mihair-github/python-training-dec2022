import legb  # import module
import math


IMPORTS_VAR = "test"

legb.my_func(10)
print(legb.X, legb.__name__)
print(math.sqrt(9))


# from legb import MyClass, X  # import names from module
# from math import sqrt
#
# my_obj = MyClass()
# print(my_obj, X)
# print(sqrt(9))


# import legb as utils  # import module as alias
# import math as mathematical_functions
#
# utils.my_func(10)
# print(utils.X, utils.__name__)
# print(mathematical_functions.sqrt(9))


# from legb import MyClass as ClassAlias  # import name as alias from module
# from math import sqrt as square_root
# import sys
#
#
# my_obj = ClassAlias()
# print(my_obj)
# print(square_root(9))
# # print("Current namespace:", globals())
# for path in sys.path:
#     print(path)


# from examples import legb  # from package import module
# from solutions import day1_string
#
# print(legb.X)


# import pypackage  # import package
# when importing packages, modules inside them are not automatically imported


# import pypackage.pymodule
# print(pypackage.pymodule.Y)
# print(pypackage.Z)


# from pypackage import pymodule
# print(pymodule.Y)


# from pypackage.pymodule import Y
# print(Y)
