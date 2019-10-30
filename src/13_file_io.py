"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

with open('foo.txt') as f:
    global read_data
    read_data = f.read()


print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

b = open('bar.txt', "w")
b.write("I bite my thumb at you sir!\n")
b.write("I bite my thumb at you!\n")
b.write("R U listening?\n")
b.close()

# print(b.read())
