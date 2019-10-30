def foo(arg1, **kwargs):
    print(arg1)
    for k, v in kwargs.items():
        print("%s == %s" % (k, v))


foo("here I am", a='Rory', b="is", c="the homie")


def bar(a, b, c):
    print("a is:", a)
    print("b is:", b)
    print("c is:", c)


kwargs = {"a": "dis one", "b": "anotha one", "c": "we da best music!"}

bar(**kwargs)


def f2(*args):
    return sum(args)


print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

print(f2(*a))    # Should print 22


def f2a(*args):
    for arg in args:
        print("f2a arg:", arg)


# What thing do you have to add to make this work?
print(f2a(a))    # Should print 22
