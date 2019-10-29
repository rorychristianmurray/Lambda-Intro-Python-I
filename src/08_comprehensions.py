"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

arr = [2, 3, 4, 5, 6]
y = [x for x in range(1, 6)]
z = [x-1 for x in arr]
w = list(map(lambda x: x, range(1, 6)))

print("y:", y)
print("z:", z)
print("w:", w)


a = ["Mali", "Rory", "Nate", "York", "Dustin", "Jamie", "Crawford", "Javontay"]
for i in a[4:]:
    print(f"We have {i} left to go")

m = [i for i in a[4:]]
print(f"We have{m} to go")
# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [x**3 for x in range(9)]
z = list(map(lambda x: x**3, range(9)))

print("cubes y:", y)
print("cubes z:", z)


# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [x.upper() for x in a]

print("upper:", y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

# x = input("Enter comma-separated numbers: ").split(',')

l = list([1, 9, 27, 3, 147, 21948932, 238, 54, 2, 3, 54535, 23344, 543543])
print("l", l)

# What do you need between the square brackets to make it work?
y = [x for x in l if x % 2 == 0]

print(y)
