i = 5

def f(arg = i):
	print(arg)

i = 6

f()

def kwarg(x, y, z):
	print(y)

kwarg(x = 3, z = 5, y = 4)
 