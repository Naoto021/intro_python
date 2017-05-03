def func():
	spam = "do_local関数の上"
	def do_local():
		nonlocal spam
		spam = "do_local関数の中"
		print("print1 " + spam)
	do_local()
	print("print2 " + spam)
		
spam = "func関数の下"
func()
print("print3 " + spam)