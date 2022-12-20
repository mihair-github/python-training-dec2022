grade = 7

if grade == 10 or grade > 20 and grade > 0:
    print('Wow! Maximum grade!')
    print('Great!')

print('Previous if-block closed')

if grade >= 7:
    print('Good job!')
elif grade >= 5:
    print('You could have done better.')
else:
    print('Oh, no! :(')


x = 5
print("It's the final countdown!")
while x != 100:
    print(x)
    x += 5
print("Boom!")

greeting = 'hello'
for character in greeting:  # for element in iterable/sequence:
    print(character)

print("range(3, 7):")
for i in range(3, 7):
    print(i)

print("range(0, 9, 3):")
for i in range(0, 9, 3):
    print(i)

print("range(3, 7) and break for 5:")
for i in range(3, 7):
    if i == 5:
        break
    print(i)

print("all numbers between 19 and 1, except multiples of 7 (while)")
x = 20
while x > 0:
    x -= 1
    if x % 7 == 0:
        continue
    print(x)

print("all numbers between 19 and 1, except multiples of 7 (for)")
for x in range(19, 0, -1):
    if x % 7 == 0:
        continue
    print(x)
