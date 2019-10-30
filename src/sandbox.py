def foo(**kwargs):
    for k, v in kwargs.items():
        print("%s == %s" % (k, v))


foo(a='Rory', b="is", c="the homie")
