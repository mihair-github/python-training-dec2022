"""
This is a docstring for module script.py
"""

print("Hello world")

# implicit line joining
text = ("If we have a long logical line, we can split it into physical lines "
        "by using the backslash at the end of the line so that Python "
        "understands that the next physical line should be considered as part "
        "of the current logical line.")
my_shopping_list = ['apples', 'bananas', 'oranges', 'pears', 'peaches',
                    'cherries']

# explicit line joining - using \
text_2 = "If we have a long logical line, we can split it into physical lines"\
         " by using the backslash at the end of the line so that Python"\
         " understands that the next physical line should be considered as "\
         "part of the current logical line."

x = 0

if x > 0:
    print("yes")
    print("still under if")

print("outside if")

multiline_str = """
abs(x) (absolute value)
int(x) (conversion to integer)
float(x) (conversion to floating point)
"""
print(multiline_str)

print("Escape double quote: \"; Escape backslash: \\")

my_str = "absolute value"
print("Substring in string:", "subs" in my_str)
