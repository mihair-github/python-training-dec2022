try:
    name = input("What is your name? ")
    print(name[5])
except (IndexError, AttributeError) as ex:
    print("Exception occurred:", ex)
except KeyboardInterrupt:
    print("Program was forcefully interrupted.")
else:
    print("No exception.")
finally:
    print("Executes every time.")
