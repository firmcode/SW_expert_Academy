a = 0
b = 20
def test():
	global a,b
	a=b
	print(a)
	#a=10


print(a)
test()
print(a)