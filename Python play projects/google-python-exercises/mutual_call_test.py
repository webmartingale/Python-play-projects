
#global limit
limit=7
#global n
n=0

def foo():
	global n
	global limit
	n = n+1	
	print n, ' foo()'	
	if n < limit:
		bar()

def bar():
	global n
	global limit
	n = n+1
	print n, ' bar()'	
	if n < limit:
		foo()
		
def main():
	print 'main()'
	print 'n = ', n
	print 'limit= ', limit
	foo()
	
if __name__ == '__main__':
	main()