n = 0
t = 0
while (n <1000):
	if (n%3 == 0 or n%5 == 0):
		t += n
	n += 1
print "sum:",t