def allparams(a, b, /, c=42, *args, d=256, e, **kwargs):
    print("a, b", a, b)
    print("c", c)
    print("d, e", d, e)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2, e=7)
allparams(1, 2, e=7, k=90)
allparams(1, 2, 3, e=7)
allparams(1, 2, c=7, e=7)
allparams(1, 2, 7, 10, 11, 12, 13, 14, 15, 27, 28, 29, e=7)
allparams(1, 2, 7, 10, 11, 12, 13, 14, 15, 27, 28, 29, d=12, e=7)
allparams(1, 2, 7, 10, 11, 12, 13, f=56, d=12, e=7, root="/")
allparams(1, 2, 7, args=(10, 11, 12, 13), f=56, d=12, e=7, root="/")


