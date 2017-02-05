def F(n):
	# Base cases
    if n == 0: return 0
    elif n == 1: return 1

    
    else: return F(n-1)+F(n-2)


for i in range(20):
	ff =  F(i)
	print "The ",i," th fib number ",ff