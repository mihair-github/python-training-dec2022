### Control structures exercises
1. Write a Python program for checking the speed of drivers. 
    * If speed is less than or equal to 50, it should print `"OK"`.
    * Otherwise, for every 5 km above the speed limit (50), it should give the 
    driver one demerit point and print the total number of demerit points. 
    For example, if the speed is 60, it should print: `"Points: 2"`.
    * If the driver gets more than 12 points, it should print: 
    `"License suspended"`
 
    Define a variable called `speed` and assign an integer value to it. 
    After running the program once, change its value and notice the changed output.
 
1. Write a Python program which iterates the integers from 1 to 50 and prints their value. 
 For multiples of three print `"Fizz"` instead of the number and for the 
 multiples of five print `"Buzz"`. For numbers which are multiples of both three
 and five print `"FizzBuzz"`. If the number 30 is encountered, break the loop.

  Output example: `1 2 Fizz 4 Buzz [...] 13 14 FizzBuzz 16 [...]`


### `try` statement exercises
1. Write a program to read two numbers: `x` and `y` from standard input and print the result of `x / y`. 
If the user inputs invalid data, display an error message and exit gracefully. 
2. Modify the previous program so that it asks the user to re-enter data until valid.

### Lists exercises
1. Given the following list:
    ```python
    l = [4, 6, 1, 7, 8, 2, 8, 2, 4, 6, 8, 9]
    ```
    * Add elements from `[5, 7, 8]` to the end of the list
    * Print the length of the list
    * Check if `8` is in the list
    * Print the first position of `7` in the list
    * Count how many times `8` is in the list
    * Reverse the list
    * Sort the list
    * Remove items on last two positions
2. Write a Python program to find the second-smallest number in a list.
3. Write a Python program to convert a list of characters into a string.
4. Given two lists, create a list of tuples where element on position `n` is a
tuple of elements on position `n` from each list. If one list is longer than the
other, ignore extra elements.

    E.g. `["Anna", "John", "Marie"]`, `[12, 15, 22, 13]` -> 
         `[("Anna", 12), ("John", 15), ("Marie", 22)]`

### Sets exercises
1. Given the following set:
    ```python
    s = set()
    ```
    * Add elements from `[1, 2, 3]` to the set
    * Print the length of the set
    * Check if `4` is in the set
    * Remove and print an arbitrary element from the set
    * Remove all remaining items in the set
1. Write a Python program that counts the number of distinct words from a string.
A word=a sequence of characters that is not whitespace (space, newline, tab).
    
    E.g. 
    ```python
    my_str = """beautiful is better than ugly
    explicit is better than implicit
    simple is better than complex
    complex is better than complicated
    flat is better than nested
    sparse is better than dense"""
    # Should print: 14 distinct words
    ```

### Dicts exercises
1. Given the following dictionary:
    ```python
    d = {
      'times': 100, 
      'name': 'George', 
      'hobbies': ['fishing', 'hiking'],
    }
    ```
    * add key `'friends'` to `d` with `['Andrei', 'Mihai', 'Alina']` as value
    * sort value for key `'friends'`
    * remove `'hiking'` from hobbies list
    * remove `'times'` key from `d`
1. Given a list of strings build a dictionary that has each unique string as a key and the 
number of appearances as a value.
    
     E.g. `['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']` ->
`{'hello': 2, 'is': 1, 'there': 2, 'anybody': 1, 'in': 1}`
